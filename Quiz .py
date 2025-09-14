import random
#parent Class
class __Quiz: 
	
	def start_quiz(self,easy,hard):
		score=0
		#creates list with 2 random question
		key_easy=random.sample(list(easy.keys()),2)
		key_hard=random.sample(list(hard.keys()),2)
		
		#Easy question
		for key in key_easy:
			print(f"\nQues) {key}")
			
			#prints all 4 options
			for i in range(4):
				print(f"{i+1}. {easy[key][i]}")
				
			#Keeps taking input untill a valid input is entered
			while True:
				try:
					Ans = int(input("Choose an option: "))
					if 1 <= Ans <= 4:
						break
					else:
						print("Not a valid option Please try again.")
				except ValueError:
					print("Enter an integer option")

            # +1 score for correct answer 		
			if easy[key][Ans-1]==easy[key][4]:
				score+=1
		
		#hard question
		for key in key_hard:
			print(f"\nQues){key}")
			for i in range(4):
				print(f"{i+1}. {hard[key][i]}")
			while True:
				try:
					Ans = int(input("Choose an option: "))
					if 1 <= Ans <= 4:
						break
					else:
						print("Not a valid option Please try again.")
				except ValueError:
					print("Enter an integer option")
			if hard[key][Ans-1]==hard[key][4]:
				score+=1
		print(f"The Quiz Ended \n Here is your Result {score}")
class coding(__Quiz):
    def __init__(self):
		#question dictionary with correct answers at last of the list in value
        self.easy = {
    "In Python, what is the output of print(2+3)?": ["23", "5", "2+3", "Error", "5"],
    "Which symbol is used for comments in C++?": ["//", "#", "<!-- -->", "%", "//"],
    "What does HTML stand for?": ["HighText Machine Language", "HyperText and Links Markup Language", "HyperText Markup Language", "None of the above", "HyperText Markup Language"]}

        self.hard = {
    "What is the time complexity of binary search?": ["O(n)", "O(log n)", "O(n^2)", "O(1)", "O(log n)"],
    "In Python, what is the difference between == and is?": ["Both are the same", "== checks value equality, is checks identity", "is checks value equality, == checks identity", "None of the above", "== checks value equality, is checks identity"],
    "Which of these best describes recursion?": ["A loop that runs forever", "A function calling itself", "Repeating code without a loop", "A function that never ends", "A function calling itself"]}

    def start_quiz(self):
		#triggers start_quiz method of Quiz class
        super().start_quiz(self.easy,self.hard)

class cricket(__Quiz):
    def __init__(self):
        self.easy = {
    "How many players are there in a cricket team?": ["9", "10", "11", "12", "11"],
    "Who is called the 'God of Cricket'?": ["MS Dhoni", "Virat Kohli", "Sachin Tendulkar", "Ricky Ponting", "Sachin Tendulkar"],
    "In which country did cricket originate?": ["India", "England", "Australia", "South Africa", "England"]}
        self.hard = {
    "Who was the first bowler to take 10 wickets in a single Test innings?": ["Jim Laker", "Anil Kumble", "Shane Warne", "Muttiah Muralitharan", "Jim Laker"],
    "Which player has scored the fastest century in ODI cricket?": ["Virat Kohli", "AB de Villiers", "Chris Gayle", "Shahid Afridi", "AB de Villiers"],
    "Who was the captain of India during the 1983 World Cup win?": ["Sunil Gavaskar", "Sourav Ganguly", "Kapil Dev", "Ravi Shastri", "Kapil Dev"]}
    def start_quiz(self):
        super().start_quiz(self.easy,self.hard)

class gk(__Quiz):
    def __init__(self):
        self.easy = {
	    "What is the capital of Japan?": ["Seoul", "Tokyo", "Beijing", "Bangkok", "Tokyo"],
	    "Who is known as the 'Father of the Nation' in India?": ["Bhagat Singh", "Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", "Mahatma Gandhi"],
	    "How many continents are there in the world?": ["5", "6", "7", "8", "7"]}
        self.hard = {
	    "Which country has the longest coastline in the world?": ["Australia", "Canada", "Russia", "Indonesia", "Canada"],
	    "Who was the first woman to win a Nobel Prize?": ["Mother Teresa", "Marie Curie", "Rosalind Franklin", "Jane Addams", "Marie Curie"],
	    "In which year was the United Nations established?": ["1919", "1939", "1945", "1950", "1945"]}
    def start_quiz(self):
        super().start_quiz(self.easy,self.hard)


print(""" \tQuiz 
    Choose between the following topics:
    1. GK
    2. Cricket 
    3. Coding   """)
while True:
    try:
        input_value=input().lower()
        if input_value=='gk'or input_value=='cricket' or input_value=='coding':
            break
        else:
            print("Not a valid option Please try again.")
    except ValueError:
        print("Enter a Valid Option")
    

if input_value=='gk':
	obj=gk()
	obj.start_quiz()
if input_value=='cricket':
	obj=cricket()
	obj.start_quiz()
if input_value=='coding':
	obj=coding()
	obj.start_quiz()