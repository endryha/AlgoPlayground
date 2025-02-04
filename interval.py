class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        yield self.start
        yield self.end

    def __getitem__(self, index):
        if index == 0:
            return self.start
        elif index == 1:
            return self.end
        else:
            raise IndexError("Index out of range. Interval only has two elements.")

    def __len__(self):
        return 2

    def __str__(self):
        return f"{self.start}..{self.end}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


def create_intervals(tuple_list):
    """
    Given a list of tuples, each representing (start, end),
    create and return a list of corresponding Interval objects.

    Parameters:
        tuple_list (list of tuple): Each tuple should have two integers (start, end)

    Returns:
        list of Interval: A list of Interval objects.
    """
    intervals = []
    for tup in tuple_list:
        if len(tup) != 2:
            raise ValueError(f"Tuple {tup} does not have exactly two elements.")
        start, end = tup
        intervals.append(Interval(start, end))
    return intervals


def draw_intervals(intervals, start_x_idx: int = None, end_x_idx: int = None):
    """
    Draws a set of Interval objects on the console as an x,y plot.

    Each interval is drawn on its own row with a y-axis label.
    The first interval (index 0) is printed at the top,
    and the last interval at the bottom.

    The x-axis spans from the smallest start to the largest end among all intervals,
    using fixed-width cells (based on the largest number) so that the dash line
    and numeric labels line up nicely.

    Before drawing the plot, the function prints the list of interval objects.

    Parameters:
        intervals (list of Interval): A list of Interval objects.
    """
    # Print the list of interval objects
    print(intervals)
    print()  # Blank line for readability

    # Determine the overall x-range.
    min_x = start_x_idx if start_x_idx is not None and start_x_idx >= 0 else min(
        interval.start for interval in intervals)
    # min_x = min(interval.start for interval in intervals)
    # min_x = 0
    max_x = end_x_idx if end_x_idx is not None and end_x_idx >= 0 else max(interval.end for interval in intervals)
    num_cells = max_x - min_x + 1

    # Determine the fixed cell width based on the largest number.
    cell_width = max(2, len(str(max_x)))

    # Draw each interval (first interval at the top).
    for idx, interval in enumerate(intervals):
        row_cells = []
        for x in range(min_x, max_x + 1):
            if interval.start <= x <= interval.end:
                cell = "*" * cell_width  # Mark with asterisks if within the interval
            else:
                cell = " " * cell_width  # Blank cell if outside the interval
            row_cells.append(cell)
        print(f"{idx:2d} | " + "".join(row_cells))

    # Draw the x-axis below the interval rows.
    margin = " " * 4  # Aligns with the y-axis labels and the vertical bar.
    dash_line = margin + " " + "-" * (cell_width * num_cells)
    print(dash_line)

    # Draw the x-axis numeric labels, centered in their fixed-width cells.
    label_cells = []
    for x in range(min_x, max_x + 1):
        label_cells.append(str(x).center(cell_width))
    x_labels = margin + " " + "".join(label_cells)
    print(x_labels)


# Example usage:
if __name__ == "__main__":
    intervals = [Interval(2, 7), Interval(5, 10), Interval(0, 3)]
    draw_intervals(intervals)
