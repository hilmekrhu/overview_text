import sublime, sublime_plugin

class OverviewTextCommand(sublime_plugin.TextCommand):
	"""Creates big letters in ASCII art style.
	Should be useful to create notes for overview.
	One line in overview can be up to 10 characters.
	"""

	def run(self, edit):


		letter_A = ["       AA       ",
					"      AAAA      ",
					"     AA  AA     ",
					"    AA    AA    ",
					"   AAA    AAA   ",
					"  AAAAAAAAAAAA  ",
					" AAA        AAA ",
					" AAA        AAA "]

		letter_B = [" BBBBBBBBBB     ",
					" BBB      BBB   ",
					" BBB      BBB   ",
					" BBBBBBBBBB     ",
					" BBB      BBB   ",
					" BBB       BBB  ",
					" BBB       BBB  ",
					" BBBBBBBBBBBB   "]

		letter_C = ["   CCCCCCCCCC   ",
					"  CCC      CC   ",
					" CCC            ",
					" CCC            ",
					" CCC            ",
					" CCC            ",
					"  CCC      CC   ",
					"   CCCCCCCCCC   "]

		letter_D = [" DDDDDDDDDD     ",
					" DDD      DDD   ",
					" DDD       DDD  ",
					" DDD       DDD  ",
					" DDD       DDD  ",
					" DDD       DDD  ",
					" DDD      DDD   ",
					" DDDDDDDDDD     "]

		letter_E = ["  EEEEEEEEEEEE  ",
					"  EEE       EE  ",
					"  EEE           ",
					"  EEEEEEEE      ",
					"  EEE           ",
					"  EEE           ",
					"  EEE       EE  ",
					"  EEEEEEEEEEEE  "]

		letter_F = ["  FFFFFFFFFFFF  ",
					"  FFF       FF  ",
					"  FFF           ",
					"  FFFFFFFF      ",
					"  FFF           ",
					"  FFF           ",
					"  FFF           ",
					"  FFF           "]

		letter_G = ["   GGGGGGGGGGG  ",
					"  GGG       GG  ",
					" GGG            ",
					" GGG            ",
					" GGG     GGGGG  ",
					" GGG        GG  ",
					"  GGG       GG  ",
					"   GGGGGGGGGGG  "]

		letter_H = [" HHH       HHH  ",
					" HHH       HHH  ",
					" HHH       HHH  ",
					" HHHHHHHHHHHHH  ",
					" HHH       HHH  ",
					" HHH       HHH  ",
					" HHH       HHH  ",
					" HHH       HHH  "]

		letter_I = ["   IIIIIIIII    ",
					"      III       ",
					"      III       ",
					"      III       ",
					"      III       ",
					"      III       ",
					"      III       ",
					"   IIIIIIIII    "]

		letter_J = ["  JJJJJJJJJJ    ",
					"          JJJ   ",
					"          JJJ   ",
					"          JJJ   ",
					"          JJJ   ",
					"  J       JJJ   ",
					"  JJ     JJJ    ",
					"   JJJJJJJ      "]

		letter_K = ["  KKK     KKK   ",
					"  KKK    KKK    ",
					"  KKK   KKK     ",
					"  KKKKKKKK      ",
					"  KKKKKKKKK     ",
					"  KKK   KKKK    ",
					"  KKK    KKKK   ",
					"  KKK     KKKK  "]


		letter_L = [" LLL            ",
					" LLL            ",
					" LLL            ",
					" LLL            ",
					" LLL            ",
					" LLL            ",
					" LLL        LL  ",
					" LLLLLLLLLLLLL  "]

		letter_M = [" MMMMM    MMMMM ",
					" MMMMMM  MMMMMM ",
					" MMM MMMMMM MMM ",
					" MMM  MMMM  MMM ",
					" MMM   MM   MMM ",
					" MMM        MMM ",
					" MMM        MMM ",
					" MMM        MMM "]

		letter_N = ["  NNNN     NNN  ",
					"  NNNNN    NNN  ",
					"  NNNNNN   NNN  ",
					"  NNN NNN  NNN  ",
					"  NNN  NNN NNN  ",
					"  NNN   NNNNNN  ",
					"  NNN    NNNNN  ",
					"  NNN     NNNN  "]

		letter_O = ["   OOOOOOOOOO   ",
					"  OOO      OOO  ",
					" OOO        OOO ",
					" OOO        OOO ",
					" OOO        OOO ",
					" OOO        OOO ",
					"  OOO      OOO  ",
					"   OOOOOOOOOO   "]

		letter_P = ["  PPPPPPPPP     ",
					"  PPP     PPP   ",
					"  PPP     PPP   ",
					"  PPP     PPP   ",
					"  PPPPPPPPP     ",
					"  PPP           ",
					"  PPP           ",
					"  PPP           "]		

		letter_Q = ["   QQQQQQQQQQ   ",
					"  QQQ      QQQ  ",
					" QQQ        QQQ ",
					" QQQ        QQQ ",
					" QQQ    QQ  QQQ ",
					" QQQ     QQ QQQ ",
					"  QQQ     QQQQ  ",
					"   QQQQQQQQ  QQQ"]

		letter_R = ["  RRRRRRRRR     ",
					"  RRR     RRR   ",
					"  RRR     RRR   ",
					"  RRR     RRR   ",
					"  RRRRRRRRR     ",
					"  RRR    RRRR   ",
					"  RRR     RRRR  ",
					"  RRR      RRR  "]		

		letter_S = ["   SSSSSSSSSS   ",
					"  SSSS      S   ",
					"   SSSS         ",
					"    SSSSSSS     ",
					"        SSSSS   ",
					"          SSSS  ",
					"  S       SSSS  ",
					"  SSSSSSSSSSS   "]							

		letter_T = [" TTTTTTTTTTTTTT ",
					" T    TTT     T ",
					"      TTT       ",
					"      TTT       ",
					"      TTT       ",
					"      TTT       ",
					"      TTT       ",
					"      TTT       "]	

		letter_U = [" UUU        UUU ",
					" UUU        UUU ",
					" UUU        UUU ",
					" UUU        UUU ",
					" UUU        UUU ",
					" UUU        UUU ",
					"  UUU      UUU  ",
					"   UUUUUUUUUU   "]		

		letter_V = [" VVV        VVV ",
					" VVV        VVV ",
					"  VVV      VVV  ",
					"   VVV    VVV   ",
					"    VVV  VVV    ",
					"     VVVVVV     ",
					"      VVVV      ",
					"       VV       "]		

		letter_W = [" WWW         WWW ",
					" WWW         WWW ",
					" WWW         WWW ",
					" WWW         WWW ",
					" WWW   WWWW  WWW ",
					" WWW WWW WWW WWW ",
					" WWWWWW   WWWWWW ",
					" WWWWW     WWWWW "]		

		letter_X = ["  XXX       XXX  ",
					"   XXX     XXX   ",
					"    XXX   XXX    ",
					"     XXXXXXX     ",
					"     XXXXXXX     ",
					"    XXX   XXX    ",
					"   XXX     XXX   ",
					"  XXX       XXX  "]		

		letter_Y = ["  YYY       YYY  ",
					"   YYY     YYY   ",
					"    YYY   YYY    ",
					"     YYYYYYY     ",
					"       YYY       ",
					"       YYY       ",
					"       YYY       ",
					"       YYY       "]		

		letter_Z = ["  ZZZZZZZZZZZZZ  ",
					"            ZZZ  ",
					"          ZZZ    ",
					"        ZZZ      ",
					"      ZZZ        ",
					"    ZZZ          ",
					"  ZZZ            ",
					"  ZZZZZZZZZZZZZ  "]		

		alphabet = { "A" : letter_A,
					 "B" : letter_B, 
					 "C" : letter_C, 
					 "D" : letter_D, 
					 "E" : letter_E, 
					 "F" : letter_F, 
					 "G" : letter_G, 
					 "H" : letter_H, 
					 "I" : letter_I, 
					 "J" : letter_J, 
					 "K" : letter_K, 
					 "L" : letter_L, 
					 "M" : letter_M, 
					 "N" : letter_N, 
					 "O" : letter_O, 
					 "P" : letter_P, 
					 "Q" : letter_Q, 
					 "R" : letter_R, 
					 "S" : letter_S, 
					 "T" : letter_T, 
					 "U" : letter_U, 
					 "V" : letter_V, 
					 "W" : letter_W, 
					 "X" : letter_X, 
					 "Y" : letter_Y, 
					 "Z" : letter_Z}

		v = self.view
		begin_marker = "/*"
		line_marker = "*"
		end_marker = "*/"

		def line (index, input_string):
			"Creates big text's line from input string, index [0;7]"
			return " ".join([alphabet[letter][index] for letter in input_string])

		# Get the seleceted text, generate big letter lines
		input = v.substr(v.sel()[0])
		lines = [line(i, input) for i in range(8)]

		# Remember text position, delete text
		start = v.sel()[0].begin()
		v.erase(edit, v.sel()[0])

		# Write result
		offset = v.insert(edit, start, "\n%s\n * " % begin_marker)	  # 1st line
		offset += v.insert(edit, start + offset, "\n * ".join(lines)) # text
		v.insert(edit, start + offset, "\n%s\n " % end_marker)		  # last line

