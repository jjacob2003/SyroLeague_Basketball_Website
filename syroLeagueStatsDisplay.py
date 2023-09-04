def display_table(headers, data):
    header_format = "{:<15}" * len(headers)
    print(header_format.format(*headers))
    for row in data:
        row_format = "{:<15}" * len(row)
        print(row_format.format(*row))

# Sample data
data = [
    ["Kevin", 7, 11.9, 3.9, 6.0, 1.9, 0.0, 1.4, "41.7%", 10],
    ["Joel D", 6, 15.8, 3.8, 0.3, 0.8, 0.0, 1.8, "45.9%", 11],
    ["Abin", 5, 14.6, 13.0, 1.2, 0.8, 0.4, 0.2, "40.0%", 1],
    ["James Moon", 6, 10.8, 8.3, 1.7, 1.5, 0.3, 1.2, "71.4%", 7],
    ["Vimel Simon", 8, 9.0, 2.2, 1.4, 0.2, 0.0, 1.4, "64.3%", 11],
    ["Amel Simon", 7, 11.0, 6.9, 1.6, 0.6, 1.0, 0.4, "36.4%", 3],
    ["Anand Matthew", 7, 9.7, 7.0, 0.9, 1.0, 2.0, 0.9, "20.0%", 6],
    ["Jacob J", 6, 6.2, 9.8, 0.8, 0.2, 0.0, 0.0, "38.5%", 0],
    ["Joshua T", 8, 4.6, 6.2, 0.8, 0.8, 0.4, 0.1, "66.7%", 1],
    ["Jubin", 7, 8.6, 3.1, 0.6, 0.1, 0.1, 1.1, "52.9%", 8],
    ["Rubin", 8, 12.1, 5.6, 2.2, 2.4, 0.6, 1.2, "62.1%", 10],
    ["Adarsh", 5, 8.6, 6.4, 3.4, 1.0, 0.8, 1.8, "35.7%", 9],
    ["Nathan S", 7, 6.4, 11.3, 2.4, 1.1, 0.1, 0.6, "70.0%", 4],
    ["Subin", 5, 15.4, 6.2, 3.6, 1.0, 0.8, 1.0, "52.9%", 5],
    ["Edwin", 8, 14.8, 6.1, 4.8, 4.8, 0.9, 1.9, "61.5%", 15],
]

headers = [
    "Player",
    "Games Played",
    "Points",
    "Rebounds",
    "Assists",
    "Steals",
    "Blocks",
    "3PT Per Game",
    "FT %",
    "Total 3s",
]

# Display the table
display_table(headers, data)