def print_board(board):
	for row in board:
		print(" | ".join(row))
		print("-" * 9)


def winner(board, player):
	lines = board + [list(column) for column in zip(*board)]
	lines += [
		[board[0][0], board[1][1], board[2][2]],
		[board[0][2], board[1][1], board[2][0]],
	]
	return [player] * 3 in lines


def play():
	board = [[" " for _ in range(3)] for _ in range(3)]
	player = "X"

	for turn in range(9):
		print_board(board)
		while True:
			try:
				move = input(f"Player {player}, choose a position (1-9): ")
				position = int(move) - 1
				row, column = divmod(position, 3)
				if 0 <= position < 9 and board[row][column] == " ":
					board[row][column] = player
					break
				print("Choose an empty position from 1 to 9.")
			except (ValueError, EOFError):
				print("Enter a number from 1 to 9.")

		if winner(board, player):
			print_board(board)
			print(f"Player {player} wins!")
			return
		player = "O" if player == "X" else "X"

	print_board(board)
	print("It's a draw!")


if __name__ == "__main__":
	play()
