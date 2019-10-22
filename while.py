bank = 1000
hand = 200
eligible = 500
y = 'y'
i = raw_input("do you want to strt the game")
while i == y:
    
      print("starting the game.......")
      if hand <= eligible:
         print("Wallet balance are less %d and adding some mony from bank  --" % (hand))
         ad = eligible - hand
         hand = hand + ad
         bank = bank - ad
         print("Wallet is now  loaded  from bank and vallet balance is %d --" % (hand))
    
