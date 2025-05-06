from datetime import datetime, timedelta, date


class SleepCalculator:
    CYCLE_MINUTES = 90
    REST_MINUTES = 15

    def __init__(self):
        self.sleep_time: datetime = datetime.now()
        self.cycles: int = 0

    def get_time_input(self) -> None:
        """Prompt user for sleep time, ensuring it's not in the past."""
        while True:
            user_input = input("Enter sleep time (HH:MM or 'n' for now): ").strip().lower()
            if user_input == "n":
                # self.sleep_time is set to datetime.now() by default
                break
            try:
                time_obj = datetime.strptime(user_input, "%H:%M").time()
                temp_time = datetime.combine(date.today(), time_obj)
                if temp_time < datetime.now():
                    print("⚠️ Selected time is in the past. Use 'n' for current time.")
                else:
                    self.sleep_time = temp_time
                    break
            except ValueError:
                print("Invalid format. Use HH:MM (e.g., 23:15).")

    def get_cycle_input(self) -> None:
        """Prompt user for number of cycles (must be ≥ 1)."""
        while True:
            try:
                cycles = int(input("How many sleep cycles? (1, 2, 3...): "))
                if cycles > 0:
                    self.cycles = cycles
                    break
                else:
                    print("Number of cycles must be positive.")
            except ValueError:
                print("Invalid input. Enter a whole number.")

    def calculate_wake_up_times(self) -> list[datetime]:
        """Calculate wake-up times for valid cycles (current ±1, if applicable)."""
        base_time = self.sleep_time + timedelta(minutes=self.REST_MINUTES)
        valid_deltas = []
        if self.cycles > 1:
            valid_deltas.append(-1)
        valid_deltas.extend([0, 1])
        return [
            base_time + timedelta(minutes=self.CYCLE_MINUTES * (self.cycles + delta))
            for delta in valid_deltas
        ]

    def display_results(self, wake_up_times: list[datetime]) -> None:
        """Display formatted wake-up options."""
        print("\n" + "≡" * 50)
        print(f" Ideal wake-up time: {wake_up_times[-2].strftime('%H:%M')} ({self.cycles} cycles)")

        if len(wake_up_times) == 3:
            print(f" Earlier option:     {wake_up_times[0].strftime('%H:%M')} ({self.cycles - 1} cycles)")
        else:
            print(" Earlier option:     N/A (minimum 1 cycle)")

        print(f" Later option:       {wake_up_times[-1].strftime('%H:%M')} ({self.cycles + 1} cycles)")
        print("≡" * 50)

    def run(self) -> None:
        """Execute the calculator workflow."""
        print("💤 Sleep Cycle Calculator 💤")
        self.get_time_input()
        self.get_cycle_input()
        wake_up_times = self.calculate_wake_up_times()
        self.display_results(wake_up_times)
        print("\nSweet dreams! 🌙")


if __name__ == "__main__":
    calculator = SleepCalculator()
    calculator.run()
