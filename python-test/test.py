#Comment
#print("Hello World")

#print("お金持ちになる")

from turtle import color
from unicodedata import name
from unittest import result
from xml.sax.handler import all_properties

from numpy import where

#from numpy import _2Tuple


unko = "Hello World"
unko_length = 5
unko_times = 5.5


#print(unko_length + unko_times)

#関数
#def unko_funbaru(arg):
#      unko_status = arg

#      if(unko_status < 10):
#        return 'mada daijobu'
#      else:
#        return 'yabai'

#print()


#list
#unko_list = ['unko_small' , 'unko_medium', 'unko_large']
#print(unko_list[1])

#for
#for index in range(11):
      #print(unko_funbaru(index))

#for item in unko_list:
#   print(item)

#with
#open()
#with open('./unko.txt' ,  'r') as file:
#   print(file.mode)



#class
#class Card: 
#      def __init__(self, date, user_name):
#        self.date = date
#        self.user_name = user_name
#      def message(self):
#        return 'この投稿は' + self.user_name + 'さんが'  + self.date + '投稿しました'

#date_a = '2020-02-072'
#user_name_a ='taro'
#card_a = Card(date_a, user_name_a)

#date_b ='2020-01-03'
#user_name_b = 'kayoko'
#card_b = Card(date_b, user_name_b)

#print(card_b.message())


#import
#import math
#print(math.pi)

#import numpy

#numpy_list = [3, 1, 5, 10, 2093, 304, 123]
#print(numpy.sum(numpy_list)



#what =input("何が:")
#when = input("いつ:")
#where = input("どこで:")
#do = input("どうした:")

#r = "{}は{}に{}で{}。" .format(what, when, where, do)
#print(r)





#def hangman(word):
#    wrong = 0
#    stages = ["",
#              "________        ",
#              "|               ",
#              "|        |      ",
#              "|        0      ",
#              "|       /|\     ",
#              "|       / \     ",
#              "|               "
#              ]
#    rletters = list(word)
#    board = ["__"] * len(word)
#    win = False
#    print("ハングマンへようこそ！")
#    while wrong < len(stages) - 1:
#        print("\n")
#        msg = "1文字を予想してね"
#        char = input(msg)
#        if char in rletters:
#            cind = rletters \
#                  .index(char)
#            board[cind] = char
#            rletters[cind] = '$'
#        else:
#            wrong += 1
#        print((" ".join(board)))
#        e = wrong + 1
#        print("\n"
#              .join(stages[0: e]))
#        if "__" not in board:
#            print("You win!")
#            print(" ".join(board))
#            win = True
#            break
#    if not win:
#        print("\n"
#              .join(stages[0: \
#              wrong]))
#        print("あなたの負け！正解は {}."
#              .format(word))
#
#hangman("L'arc~en~ciel")


#War
#from random import shuffle
#
#class Card :
#  suits = ["spades", "hearts", "diamonds", "clubs"]
#
#  values = [None, None,
#                  "2", "3", "4", "5", "6", "7", "8", "9",
#                  "10", "Jack", "Queen", "King", "Ace"]
#
#  def __init__(self, v, s):
#    """スート(マーク)も値も整数値です"""
#    self.value = v
#    self.suit = s
#
#  def _lt__(self, c2) :
#    if self.value < c2.value:
#      return True
#    if self.value == c2.value:
#      if self.suits < c2.suit:
#        return True
#      else:
#        return False
#    return False
#
#  def __gt__(self, c2) :
#    if self.value > c2.value :
#      return True
#    if self.value == c2.value:
#      if self.suit > c2.suit:
#        return True
#      else:
#        return False
#    return False
#
#  def __repr__(self) :
#    v = self.values[self.value] + " of " \
#          + self.suits[self.suit]
#    return v
#
#class Deck:
#  def __init__(self):
#    self.cards = []
#    for i in range(2, 15):
#      for j in range(4):
#        self.cards.append(Card(i, j))
#    print(shuffle(self.cards))
#
#  def rm_card(self) :
#    if len(self.cards) == 0 :
#      return
#    return self.cards.pop()
#
#class Player :
#  def __init__(self, name) :
#    self.wins = 0
#    self.card = None
#    self.name = name
#
#class Game :
#  def __init__(self) :
#    name1 = input("プレイヤー1の名前 ")
#    name2 = input("プレイヤー2の名前 ")
#    self.deck = Deck()
#    self.p1 = Player(name1)
#    self.p2 = Player(name2)
#
#  def wins(self, winner):
#    w = "このラウンドは {} が勝ちました"
#    w = w.format(winner)
#    print(w)
#
#  def draw(self, p1n, p1c, p2n, p2c):
#    d = "{} は {}、{} は {} を引きました"
#    d = d.format(p1n, p1c, p2n, p2c)
#    print(d)
#
#  def play_game(self) :
#    cards = self.deck.cards
#    print("戦争を始めます!")
#    while len(cards) >= 2:
#      m = "qで終了、それ以外のキーでPlay:"
#      response = input(m)
#      if response == 'q':
#        break
#      p1c = self.deck.rm_card()
#      p2c = self.deck.rm_card()
#      p1n = self.p1.name
#      p2n = self.p2.name
#      self.draw(p1n, p1c, p2n, p2c)
#      if p1c > p2c:
#        self.p1.wins += 1
#        self.wins(self.p1.name)
#      else:
#        self.p2.wins += 1
#        self.wins(self.p2.name)
#    win = self.winner(self.p1, self.p2)
#    print("ゲーム終了、{} の勝利です!".format(win))
#
#  def winner(self, p1, p2):
#    if p1.wins > p2.wins:
#      return p1.name
#    if p1.wins < p2.wins:
#      return p2.name
#    return "引き分け！"
#
#game = Game()
#print(game.play_game())



