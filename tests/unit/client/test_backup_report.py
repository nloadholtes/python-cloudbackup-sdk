import unittest

import rcbu.client.backup_report as backup_report
import tests.mock.report as mock_report
from rcbu.common.exceptions import BackupFailed


class TestBackupReport(unittest.TestCase):
    def setUp(self):
        mock = mock_report.backup_report(errors=['explosions'],
                                         restorable=True)
        self.report = backup_report.from_dict(1, mock)

    def test_id_matches_expected(self):
        self.assertEqual(self.report.id, 1)

    def test_state_matches_expected(self):
        self.assertEqual(self.report.state, 'Completed')

    def test_errors_match_expected(self):
        self.assertEqual(len(self.report.errors), 1)
        self.assertEqual(self.report.errors[0], 'explosions')

    def test_outcome_matches_expected(self):
        self.assertEqual(self.report.outcome, 'OK')

    def test_ok_matches_expected(self):
        self.assertEqual(self.report.ok, True)

    def test_diagnostics_matches_expected(self):
        self.assertEqual(self.report.diagnostics, 'OK')

    def test_started_matches_expected(self):
        self.assertEqual(self.report.started, '\/Date(1351118760000)\/')

    def test_ended_matches_expected(self):
        self.assertEqual(self.report.ended, '\/Date(1351118760001)\/')

    def test_duration_matches_expected(self):
        self.assertEqual(self.report.duration, '00:00:00')

    def test_does_not_raise_if_ok(self):
        self.report.raise_if_not_ok()

    def test_raises_if_not_restorable(self):
        self.report._restorable = False
        with self.assertRaises(BackupFailed):
            self.report.raise_if_not_ok()

    def test_searched_matches_expected(self):
        self.assertEqual(self.report.files_searched, 0)
        self.assertEqual(self.report.bytes_searched, 0)

    def test_stored_matches_expected(self):
        self.assertEqual(self.report.files_stored, 0)
        self.assertEqual(self.report.bytes_stored, 0)