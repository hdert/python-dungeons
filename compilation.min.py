_C=False
_B=True
_A=None
from os.path import isfile
import sqlite3
from datetime import date
from random import randint as rand
from sys import exit as sys_exit
try:import curses
except ModuleNotFoundError:from traceback import print_exc;print_exc();print('\n    You need to install windows-curses. You can do this through the\n    command:\n    `python -m pip install windows-curses`');sys_exit()
def db_create(db_path='main.db'):
	db_exists=isfile(db_path);conn=sqlite3.connect(db_path);conn.isolation_level=_A;c=conn.cursor()
	if not db_exists:c.execute('\n        CREATE TABLE leaderboard(\n            username varchar(15) NOT NULL,\n            date date NOT NULL,\n            scoreone tinyint(2) NOT NULL,\n            scoretwo tinyint(2) NOT NULL,\n            scorethree tinyint(2) NOT NULL,\n            scoretotal tinyint(2) NOT NULL\n        )\n        ')
	return c
def fetch_results(c):
	if user_binary_choice('Do you want to search by username'):username=f"%{get_username()}%";c.execute('SELECT * FROM `leaderboard`\n        WHERE `username` LIKE ?\n        ORDER BY `scoretotal` DESC, `username` ASC',[username])
	else:c.execute('SELECT * FROM `leaderboard`\n        ORDER BY `scoretotal` DESC, `username` ASC')
	results=c.fetchall()
	if not results:input('\n    No results.')
	return results
def get_username():
	while _B:
		user_input=input('\n    Please enter the username: ')
		if len(user_input)>15:input('\n    The username is too long. The username needs to be under 15 characters')
		elif len(user_input)<1:input('\n    The username is too short. The username needs to be more than 0\n    characters')
		elif user_input.isalnum()and not user_input.isnumeric():return user_input
		else:input("\n    The username doesn't contain any characters. Please use characters")
def introduction():
	input('\n    Welcome to python-quiz, your source of NCEA knowledge quizzes.\n\n    The only input in this game are the numbers 1 to 4. Each of these numbers\n    will correspond to an action or answer.\n    Try this example of navigation (press enter to continue)')
	while _B:
		user_input=input('\n    Navigation:\n    1) North: Cheese Room;\n    2) South: Exit;\n    3) East: Blocked Door;\n    4) West: Blocked Door;\n    [1-4]: ')
		if user_input=='1':input("\n    You obviously know what you're doing.");input('\n    These questions are supposed to be difficult, you should go grab something\n    to write on.');break
		if user_input=='2':input('\n    What? Escape? Why would you want to do that now?')
		elif user_input in('3','4'):input('\n    You walk into the concrete of the blocked doorway')
		else:out_of_range_error(4)
def leaderboard_entry(c,score):c.execute('INSERT INTO leaderboard VALUES (?, ?, ?, ?, ?, ?)',[get_username(),date.today(),score[0],score[1],score[2],sum(score)]);input('\n    Your score, username and the date of completion have been entered into the\n    leaderboard')
def main():
	while _B:
		score=[_A,_A,_A];introduction();location=navigate()
		while _B:
			if quiz_check(location,score):
				score=quiz(location,score)
				if score[0]is not _A and score[1]is not _A and score[2]is not _A:
					if user_binary_choice('Do you want your score saved in the leaderboard'):c=db_create();leaderboard_entry(c,score)
					if user_binary_choice('Do you want to see the leaderboard'):
						if'c'not in locals():c=db_create()
						show_leaderboard(c)
					if user_binary_choice('Do you want to play again'):return
					else:sys_exit()
			location=navigate(location)
def navigate(location=0):
	room=['Entrance','Math Room','English Room','NCEA Headquaters','Fancy Wall'];relations=[[2,4,4,4],[4,4,0,4],[3,0,4,4],[1,4,4,0]]
	try:user_input=int(input(f"""
    Navigation:
    1) North: {room[relations[0][location]]};
    2) South: {room[relations[1][location]]};
    3) East: {room[relations[2][location]]};
    4) West: {room[relations[3][location]]};
    [1-4]: """))
	except ValueError:out_of_range_error(4);return navigate(location)
	if user_input in(1,2,3,4):
		if relations[user_input-1][location]==4:input("\n    That wall sure looks like a hidden entrance. You try and activate it,\n    it doesn't react.");return navigate(location)
		return relations[user_input-1][location]
	out_of_range_error(4);return navigate(location)
def out_of_range_error(length):
	numbers=[]
	for i in range(length):numbers.append(str(i+1))
	input('\n    When prompted, enter one of the numbers {}.\n    Each number corresponds to an action printed on screen.'.format(', '.join(numbers)))
def quiz_check(location,score):
	if location==1 and score[0]is not _A or location==2 and score[1]is not _A or location==3 and score[2]is not _A:return _C
	if location==0:input("\n    You've done this room.");return _C
	return _B
def quiz(location,score):
	l='72';k='60';j='80';i='Listing';h='Emphasis';g='Humor';f='Irony';e='Imagery';d='Exaggeration';c='Preposition';b='Pronoun';a='Sonnet';Z='Imperative';Y='Hyperbole';X='Add to 360°';W='Equals 180°';V='Equals 360°';U='are equal';T='add to 180°';S='360°';R='(3x)/(x-3)';Q='(36x-23)/(12)';P='360';O='Direct speech';N='Repetition';M='Conjunction';L='Adjective';K='Have no relationship';J='Add to 120°';I='Are equal';H='180°';G='120°';F='15';E='Metaphor';D='Verb';C='Noun';B='Adverb';A='Add to 180°';quiz_questions=[['What is the correct formula to find the sum of the internal\n    angles of a polygon:','What is the correct formula to find the sum of the external\n    angles of a polygon:','Substitute u = 3 and t = 5 into the following equation:\n    d = ut + 3t²','Solve the equation 10x² - 27x - 9 = 0','What is (8x - 1)/(4) + (3x-5)/(3) as a simplified single\n    fraction','What is (3x² + 9x)/(x² - 9) as a simplified single fraction','fk² - 9c² = 4d² + 16gk², Give the equation for k in terms of c,\n    d, f, and g.','What is 3 * 5','5³','What does SOH in SOH CAH TOA stand for','What does CAH in SOH CAH TOA stand for','What does TOA in SOH CAH TOA stand for','Angles on a line add to','Angles on a point add to','Vertically opposite angles','Angles in a Triangle','Angles in a Square','An exterior angle of a triangle equals','In an isosceles triangle','Co-Interior angles on parallel lines'],['What part of speech is the word jump:','What language feature is this:\n    Go clean your room right now this instance you naughty little\n    devil child!','What type of poem is this:\n    Go clean your room right\n    now this instance you naughty\n    little devil child!','Every name is called a * as field and fountain street and town','In place of the noun the * stands as he and she can clap their\n    hands','The * describes a thing as magic wand or bridal ring','The * means action something done to read, to write, to jump,\n    to run','How things are done the * tells as quickly, slowly, badly, well','The * shows relation as in the street or at the station','* join in many ways sentences, words, phrase, and phrase','Three little words you often see are * a, an, and the','The * cries out hark! We need an exclamation mark','A type of exaggeration used in literature.','A type of figurative imagery using like, as, or than to compare\n    two separate items with one another','Saying something that is different from what you really mean','Using words that end in the same sounds','Repeating something to emphasize it','A series of words, connected in meaning and image which\n    emphasize a point','Using irony as a attack','A command to the reader or listener'],['How many credits does a Level 1 student in 2020 need:','How many credits will a Level 2 student need next year:','The Great Depression started in','Obsidian is a type of','Hyperinflation is when','The proper name of America is','Woodrow Wilson was','Team Fortress 2 is the','Mein Kampf is','The Great Depression was caused by','Armistice is','What are the three types of texts in the english external\n    unfamiliar texts','a NSN is a what','A 747 is a famous','How much water should you drink in a day','Angles on the same arc','If the angle at the center of a circle is 180° the angle at the\n    circumference equals','alternate angles on parallel lines','corresponding angles on parallel lines','Two radii in a circle will form what']];quiz_answers=[[['n - 2 * 180','(n - 2)180','n - 2 * 60',P,1],['n * 60','n + 3 * 180','(n + 3)180',P,3],[F,'30','100','90',3],['x = (-3/10) OR x = 3','x = 7','x = 3','(10x + 3)(x - 3) = 0',0],[Q,'(3(8x - 1) + 4(3x - 5))/(12)',R,'(24x - 3 + 12x - 20)/(12)',0],[Q,'(3x(x + 3))/((x+3)(x - 3))',R,'(x - 3)/(3x)',2],['k = √((4d² + 9c²)/(f - 16g))','k = (4d² + 9c²)/(f - 16g)','k = √(4d² + 9c²)','k = 4d² + 9c² - f - 16g',0],[F,'20','12','8',0],[F,'45','75','125',3],['Sin','Sine','Sine Over Hypotenuse','Sine Opposite Hypotenuse',3],['Cos','Cosine Adjacent Hypotenuse','Cosine','Cosine Against Hypotenuse',1],['Tan','Tangent Over Hypotenuse','Tangent Opposite Hypotenuse','Tangent',2],[G,H,S,'Three',1],[S,H,G,'Five',0],[T,U,'add to 360°','are not related',1],[A,V,W,X,0],[A,V,W,X,3],[G,'The sum of the two opposite angles','180° - the opposite angles','360° - the opposite angles',1],['The base angles are equal','The base angles add to 180°','The base angles - 360° equals 180°','The base angles are in a romantic relationship',0],[I,J,K,A,3]],[[C,D,L,B,1],[Y,'Rhetoric',Z,a,2],[a,'Haiku','Limerick','Free verse',1],[D,B,C,'Field',2],['clap','Article',B,b,3],[L,'Magic',M,b,0],[D,B,C,'Read',0],['Quickly',D,B,C,2],[M,'Street',c,L,2],['Conjunctions','Sentences','Prepositions','Adjectives',0],['Trains','Articles','Adverbs','Pronouns',1],[M,'Mark','Interjection',c,2],[d,Y,e,E,1],[d,e,E,'Simile',3],[f,'Innuendo',g,E,0],['Assonance','Rhythm','Rhyme',N,2],[h,i,N,O,2],[h,i,N,O,1],[f,'Sarcasm',g,E,0],[Z,'Direct address',O,'Fart',0]],[[j,k,l,'70',3],[j,k,l,'52',1],['1929','1933','1923','1928',0],['Rock','Glass','Volcanic Glass','Block used to make a nether portal',2],['The value of a local currency quickly lowers','The gas content of a stomach rapidly increases',"A country rapidly enlarges it's borders","Too many people start to work at McDonald's™",0],['The United States of America','We The People','USA','US',0],['A famous actor','A common name','A famous celebrity','The president of The United States of America (POTUS)',3],['Best game in existence','Has been in development for 19 years','And is not dead','All of the above',3],['German','A book written by Hitler','A book written by Woodrow Wilson','A famous piece of paper',1],['Hyperinflation','Mein Kampf','Hitler','The Wall Street Crash',3],['An agreement in a war to stop fighting','A form of jointed club','A type of business deal','The name for a yellow carrot',0],['Story, poem and fiction','Narrative prose, poetry and non-fiction','fiction, poetry and non-fiction','aggressive, assertive and passive',1],['National Steward Number','iNternational Scalene Nonagon','New South Nales','National Student Number',3],['Boat','Airbus Plane','Boeing Plane','Rifle',2],['2 Liters','1.5 Liters',"Enough so that you aren't thirsty",'How much you friends drink',2],['are 180°',T,U,'add to 120°',2],['80°','50°',H,'90°',3],[I,J,K,A,0],[I,J,K,A,0],['A parallelogram','A polygon','A isosceles triangle','A scalene triangle',2]]];current_questions=quiz_questions[location-1];current_answers=quiz_answers[location-1];score[location-1]=0
	while len(current_questions)>5:
		rand_choice=rand(0,len(current_questions)-1);user_input=_A
		while user_input not in(1,2,3,4):
			try:user_input=int(input(f"""
    {current_questions[rand_choice]}
    1) {current_answers[rand_choice][0]}
    2) {current_answers[rand_choice][1]}
    3) {current_answers[rand_choice][2]}
    4) {current_answers[rand_choice][3]}
    [1-4]: """))
			except ValueError:user_input=_A
			if user_input not in(1,2,3,4):out_of_range_error(4)
		if user_input-1==current_answers[rand_choice][4]:input('\n    You got it right');score[location-1]+=1
		else:input(f"\n    You got it wrong.\n    The answer was:\n    {current_answers[rand_choice][current_answers[rand_choice][4]]}")
		current_questions.pop(rand_choice);current_answers.pop(rand_choice)
	return score
def show_leaderboard(c):
	A='| {:15} | {:10} | {:13} | {:11} | {:13} | {:10} |\n';results=fetch_results(c)
	if not results:return
	try:
		stdscr=curses.initscr();curses.noecho();curses.cbreak();lines=0
		while lines<len(results):
			stdscr.addstr(A.format('Username','Date','Overall Score','Maths Score','English Score','NCEA Score'))
			for _ in range(curses.LINES-2):
				stdscr.addstr(A.format(results[lines][0],results[lines][1],results[lines][5],results[lines][2],results[lines][3],results[lines][4]));lines+=1
				if lines>=len(results):stdscr.addstr('(enter to continue)');stdscr.getkey();curses.endwin();return
			stdscr.addstr('[q]uit, [n]ew page: ');stdscr.refresh()
			while _B:
				user_input=stdscr.getkey().lower()
				if user_input=='q':curses.endwin();return
				if user_input=='n':stdscr.clear();break
	except KeyboardInterrupt:from traceback import print_exc;from sys import exit as sys_exit;curses.endwin();print_exc();sys_exit()
def user_binary_choice(x):
	while _B:
		try:user_input=int(input(f"\n    {x}:\n    1) Yes\n    2) No\n    [1-2]: "))
		except ValueError:out_of_range_error(2);return user_binary_choice(x)
		if user_input in(1,2):
			if user_input==1:return _B
			return _C
		out_of_range_error(2)
if __name__=='__main__':main()