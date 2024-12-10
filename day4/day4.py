def count_xmas_occurrences(filename):
    def search_word(grid, word):
        rows, cols = len(grid), len(grid[0])
        word_len = len(word)
        count = 0

        # Directions: right, down, diagonal down-right, diagonal down-left
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    if all(0 <= r + dr * k < rows and 0 <= c + dc * k < cols and grid[r + dr * k][c + dc * k] == word[k] for k in range(word_len)):
                        count += 1
                    # Check reverse direction
                    if all(0 <= r - dr * k < rows and 0 <= c - dc * k < cols and grid[r - dr * k][c - dc * k] == word[k] for k in range(word_len)):
                        count += 1
        return count

    with open(filename, 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    return search_word(grid, "XMAS")

# Example usage
filename = 'day4/day4_input.txt'
print(count_xmas_occurrences(filename))