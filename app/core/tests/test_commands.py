"""
Testing custom django management commands
"""

from unittest.mock import patch # mocking a behaviour

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError 
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check') #Command.check is a command from BaseCommand - it have check method - which we are mocking
class CommandTests(SimpleTestCase):

  def test_wait_for_db_ready(self,patched_check):
    patched_check.return_value = True

    call_command('wait_for_db') # calling the command

    patched_check.assert_called_once_with(databases=['default'])

  @patch('time.sleep') #wait for some time and then request again + patch gets added inside out.
  def test_wait_for_db_delay(self,patched_sleep,patched_check):
    patched_check.side_effect = [Psycopg2Error]*2 + [OperationalError]*3 + [True]
    # for the first two times we raise psy error and next time raise 3 operational error
    # for the 6th time, we are expecting a true value

    call_command('wait_for_db')

    self.assertEqual(patched_check.call_count, 6)
    patched_check.assert_called_with(databases=['default'])

