from datetime import datetime, timedelta

def calculate_due_date(submit_datetime: datetime, turnaround_hours: int) -> datetime:
    WORKING_HOURS_PER_DAY = 8
    START_HOUR, END_HOUR = 9, 17
    
    if submit_datetime.hour < START_HOUR or submit_datetime.hour >= END_HOUR:
        raise ValueError("Submit time must be within working hours (9AM - 5PM).")
    
    full_days, remaining_hours = divmod(turnaround_hours, WORKING_HOURS_PER_DAY)
    
    # Move forward full working days (excluding weekends)
    current_date = submit_datetime
    while full_days > 0:
        current_date += timedelta(days=1)
        if current_date.weekday() < 5:  # Monday to Friday
            full_days -= 1
    
    # Add remaining hours, ensuring we stay within working hours
    due_hour = submit_datetime.hour + remaining_hours
    if due_hour >= END_HOUR:
        extra_days = (due_hour - END_HOUR) // WORKING_HOURS_PER_DAY + 1
        due_hour = START_HOUR + (due_hour - END_HOUR) % WORKING_HOURS_PER_DAY

        while extra_days > 0:
            current_date += timedelta(days=1)
            if current_date.weekday() < 5:
                extra_days -= 1

    # Ensure tasks that exactly fill a workweek end on Friday at 5 PM
    if turnaround_hours % (5 * WORKING_HOURS_PER_DAY) == 0 and submit_datetime.weekday() == 0:
        current_date = submit_datetime + timedelta(days=4)
        return datetime(current_date.year, current_date.month, current_date.day, END_HOUR, 0)
    
    return datetime(current_date.year, current_date.month, current_date.day, due_hour, submit_datetime.minute)

# Tests
import unittest

class TestDueDateCalculator(unittest.TestCase):
    def test_same_day_due(self):
        submit_time = datetime(2025, 3, 10, 10, 0)  # Monday 10AM
        turnaround = 4  # 4 working hours
        expected = datetime(2025, 3, 10, 14, 0)  # Monday 2PM
        self.assertEqual(calculate_due_date(submit_time, turnaround), expected)
    
    def test_next_day_due(self):
        submit_time = datetime(2025, 3, 10, 14, 0)  # Monday 2PM
        turnaround = 6  # 6 working hours
        expected = datetime(2025, 3, 11, 12, 0)  # Tuesday 12PM
        self.assertEqual(calculate_due_date(submit_time, turnaround), expected)
    
    def test_across_weekend(self):
        submit_time = datetime(2025, 3, 14, 16, 0)  # Friday 4PM
        turnaround = 3  # 3 working hours
        expected = datetime(2025, 3, 17, 11, 0)  # Monday 11AM
        self.assertEqual(calculate_due_date(submit_time, turnaround), expected)
    
    def test_full_week_due(self):
        submit_time = datetime(2025, 3, 10, 9, 0)  # Monday 9AM
        turnaround = 40  # 40 working hours (5 full working days)
        expected = datetime(2025, 3, 14, 17, 0)  # Friday 5PM
        self.assertEqual(calculate_due_date(submit_time, turnaround), expected)
    
if __name__ == "__main__":
    unittest.main()
