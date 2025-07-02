"""
Django command to wait for the database to be available
"""
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """
    Django command to wait for db
    """
    def handle(self, *args, **options):
        """Entry point for the command. """
        self.stdout.write("Waiting for the Database. ")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write(
                    "Database is unavailable. Waiting 1 Second..."
                )
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database Available!'))
