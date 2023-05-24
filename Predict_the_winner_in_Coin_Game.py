def main():
  m, n = map(int, input().split())

  # If one of the piles has an even number of coins, then Player 1 wins.
  if m % 2 == 0 or n % 2 == 0:
    print("Player 1")
    return

  # Otherwise, Player 2 wins.
  print("Player 2")

if __name__ == "__main__":
  main()
