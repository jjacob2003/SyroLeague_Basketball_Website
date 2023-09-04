# Function to get stat lines from the user until they say "stop"
def get_stat_lines_from_user():
    print("Enter stat lines, one per line. Press Enter on an empty line to finish.")
    stat_lines = []
    while True:
        stat_line_input = input()
        if stat_line_input.strip() == "":
            break
        stat_lines.append(stat_line_input)

    return stat_lines

# Main function to calculate and display average stats for all stat lines entered by the user
def main():
    stat_lines = get_stat_lines_from_user()
    total_games_played = len(stat_lines)

    # Accumulate stats for each stat line
    total_points = 0
    total_rebounds = 0
    total_assists = 0
    total_steals = 0
    total_blocks = 0
    total_three_pointers_made = 0
    total_free_throws_made = 0
    total_free_throws_attempted = 0

    for stat_line in stat_lines:
        stats = stat_line.split()
        points, rebounds, assists, steals, blocks, three_pointers_made = map(int, stats[:6])
        free_throws_made, free_throws_attempted = map(int, stats[6].split('/'))

        total_points += points
        total_rebounds += rebounds
        total_assists += assists
        total_steals += steals
        total_blocks += blocks
        total_three_pointers_made += three_pointers_made
        total_free_throws_made += free_throws_made
        total_free_throws_attempted += free_throws_attempted

    total_games_played = len(stat_lines)

    # Calculate the overall average for each stat, rounded to one decimal place
    avg_points = round(total_points / total_games_played, 1)
    avg_rebounds = round(total_rebounds / total_games_played, 1)
    avg_assists = round(total_assists / total_games_played, 1)
    avg_steals = round(total_steals / total_games_played, 1)
    avg_blocks = round(total_blocks / total_games_played, 1)
    avg_three_pointers = round(total_three_pointers_made / total_games_played, 1)
    avg_free_throw_percentage = round((total_free_throws_made / total_free_throws_attempted) * 100, 1) if total_free_throws_attempted > 0 else 0

    # Display the overall average stats
    print("\nOverall Average Stats:")
    print(f"Total Games Played: {total_games_played}")
    print(f"Points: {avg_points}")
    print(f"Rebounds: {avg_rebounds}")
    print(f"Assists: {avg_assists}")
    print(f"Steals: {avg_steals}")
    print(f"Blocks: {avg_blocks}")
    print(f"3-Pointers Per Game: {avg_three_pointers}")
    print(f"Free Throw Percentage: {avg_free_throw_percentage:.1f}%")

    # Display total threes
    print(f"Total 3-Pointers Made: {total_three_pointers_made}")

if __name__ == "__main__":
    main()