class EmulatedTuner:
    frequency_table = [
        4884, 4921, 4958, 4990, 4995, 5020, 5032, 5050,
        5069, 5080, 5099, 5110, 5140, 5170, 5200, 5325,
        5333, 5348, 5362, 5366, 5373, 5384, 5399, 5402,
        5413, 5420, 5436, 5438, 5453, 5456, 5473, 5493,
        5510, 5533, 5547, 5573, 5584, 5613, 5621, 5645,
        5658, 5665, 5685, 5695, 5705, 5725, 5732, 5733,
        5740, 5745, 5752, 5760, 5765, 5769, 5771, 5780,
        5785, 5790, 5800, 5805, 5806, 5809, 5820, 5825,
        5828, 5840, 5843, 5845, 5847, 5860, 5865, 5865,
        5866, 5880, 5880, 5885, 5905, 5917, 5925, 5945,
        5960, 5980, 6000, 6002, 6020, 6028, 6040, 6054,
        6060,
    ]

    skip_table = []

    min_frequency_idx = 0
    max_frequency_idx = len(frequency_table) - 1
    current_frequency_idx = min_frequency_idx

    def __init__(self, rssi_threshold, min_idx, max_idx):
        self.min_frequency_idx = min_idx
        self.max_frequency_idx = max_idx
        self.rssi_threshold = rssi_threshold

        self.skip_table = []

        # set initial frequency to before step
        self.current_frequency_idx = self.min_frequency_idx

    def next(self):
        self.current_frequency_idx += 1
        if self.current_frequency_idx > self.max_frequency_idx:
            self.current_frequency_idx = self.min_frequency_idx
        if self.current_frequency_idx in self.skip_table:
            self.next()
            return

    def prev(self):
        self.current_frequency_idx -= 1
        if self.current_frequency_idx < self.min_frequency_idx:
            self.current_frequency_idx = self.max_frequency_idx
        if self.current_frequency_idx in self.skip_table:
            self.prev()
            return

    def is_signal_strong(self):
        return self.frequency_table[self.current_frequency_idx] == 5760

    def get_frequency(self):
        return self.frequency_table[self.current_frequency_idx]

    def get_frequency_idx(self):
        return self.current_frequency_idx

    def skip_frequency(self, frequency_idx):
        if frequency_idx not in self.skip_table:
            self.skip_table.append(frequency_idx)

    def clear_skip(self, frequency_idx, all_values=False):
        if all_values:
            self.skip_table = []
        else:
            if frequency_idx in self.skip_table:
                self.skip_table.remove(frequency_idx)

    def get_config(self):
        return {
            "frequency": self.get_frequency(),
            "frequency_idx": self.get_frequency_idx(),
            "rssi_threshold": self.rssi_threshold,
            "min_frequency": self.frequency_table[self.min_frequency_idx],
            "max_frequency": self.frequency_table[self.max_frequency_idx],
            "skip_table": self.skip_table
        }

    def set_rssi_threshold(self, rssi_threshold):
        self.rssi_threshold = rssi_threshold