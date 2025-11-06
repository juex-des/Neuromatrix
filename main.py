import sys, os, time, random
from fileHandler import load_file, save_file

status = 0
startTime = time.time()
quotes = [
    "\"Live as if you were to die tomorrow. Learn as if you were to live forever.\"\n – Mahatma Gandhi",
    "\"The beautiful thing about learning is nobody can take it away from you.\"\n – B.B. King",
    "\"Tell me and I forget. Teach me and I remember. Involve me and I learn.\"\n – Benjamin Franklin",
    "\"Learning never exhausts the mind.\"\n – Leonardo da Vinci",
    "\"Education is the most powerful weapon which you can use to change the world.\"\n – Nelson Mandela",
    "\"The more I read, the more I acquire, the more certain I am that I know nothing.\"\n – Voltaire",
    "\"Once you stop learning, you start dying.\"\n – Albert Einstein",
    "\"Change is the end result of all true learning.\"\n – Leo Buscaglia",
    "\"He who learns but does not think, is lost!\"\n – Confucius"
  ]

class Profile:
  def __init__(self, data):
    self.username = data["username"]
    self.date_registered = data["date_registered"]
    self.last_login = data["last_login"]
    self.last_coinflip = data["last_coinflip"]
    self.today_learning_time = data["today_learning_time"]
    self.total_learning_time = data["total_learning_time"]
    self.coin = data["coin"]
    self.streak = data["streak"]
    self.hp = data["hp"]
    self.max_hp = data["max_hp"]
    self.tier_accolade = data["tier_accolade"]
    self.boss_unlocked = data["boss_unlocked"]
    self.settings_quote = data["settings_quote"]
    self.quests_claimed = data["quests_claimed"]
    self.abilities = data["abilities"]

  def to_dict(self):
    return {
      "username": self.username,
      "date_registered": self.date_registered,
      "last_login": self.last_login,
      "last_coinflip": self.last_coinflip,
      "today_learning_time": self.today_learning_time,
      "total_learning_time": self.total_learning_time,
      "coin": self.coin,
      "streak": self.streak,
      "hp": self.hp,
      "max_hp": self.max_hp,
      "tier_accolade": self.tier_accolade,
      "boss_unlocked": self.boss_unlocked,
      "settings_quote": self.settings_quote,
      "quests_claimed": self.quests_claimed,
      "abilities": self.abilities
    }

  def save(self):
    save_file(PROFILE_FILE, self.to_dict())

  def addCoin(self, amount):
    self.coin += amount
    self.save()

  def heal(self, amount):
    self.hp = min(self.hp + amount, self.max_hp)
    self.save()

  def upgrade_ability(self, key, value):
    if key == "max_hp":
      self.max_hp = value
    else:
      self.abilities[key] = value

# loading file

testing_mode = False
if testing_mode:
  PROFILE_FILE = "userdata_forTesting/profile.json"
  GOAL_FILE = "userdata_forTesting/goal.json"
  QUEST_FILE = "userdata_forTesting/quest.json"
  QUIZ_FILE = "userdata_forTesting/quiz.json"
else:
  PROFILE_FILE = "userdata/profile.json"
  GOAL_FILE = "userdata/goal.json"
  QUEST_FILE = "userdata/quest.json"
  QUIZ_FILE = "userdata/quiz.json"

profile = Profile(load_file(PROFILE_FILE))
goal = load_file(GOAL_FILE)
quest = load_file(QUEST_FILE)
quiz = load_file(QUIZ_FILE)

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  print()

def elapsed_time(mode):
  elapsed_time = time.time() - startTime
  hours = int(elapsed_time // 3600)
  minutes = int((elapsed_time % 3600) // 60)
  seconds = int(elapsed_time % 60)

  if mode == "d":
    return f"{hours:02}h {minutes:02}m {seconds:02}s"
  elif mode == "l":
    return int(elapsed_time)
  else:
    return

def hp_bar(bar_width=10):
  ratio = profile.hp / profile.max_hp
  filled = int(ratio * bar_width)
  empty = bar_width - filled

  if ratio <= 0.4:
    color = '\033[31m'
  elif ratio <= 0.6:
    color = '\033[33m'
  else:
    color = '\033[32m'

  bar = color + '■' * filled + ' ' * empty + '\033[0m'
  return f"[{bar}]  {profile.hp}/{profile.max_hp}"

def display(mode=0):
  time.sleep(0.25)

  if os.name == 'nt':
    os.system('cls')
  elif os.name == 'posix':
    os.system('clear')

  print('\033[1;36m  NEUROMATRIX    \033[90mv1.1.0\033[0m')
  if mode == 0:
    if profile.today_learning_time < 3600:
      elapsedTimeColor = "\033[1;33m"
    elif profile.today_learning_time < 7200:
      elapsedTimeColor = "\033[1;32m"
    elif profile.today_learning_time < 9900:
      elapsedTimeColor = "\033[1;34m"
    
    hoursT = int(profile.today_learning_time // 3600)
    minutesT = int((profile.today_learning_time % 3600) // 60)
    secondsT = int(profile.today_learning_time % 60)
    print(f'🕒 Time elapsed: {elapsed_time("d")} for this session ({elapsedTimeColor}{hoursT:02}h {minutesT:02}m {secondsT:02}s\033[0m today)')
    print(f'💰 Coins:        \033[1m{profile.coin}\033[0m')
    print(f'❤️   HP:          {hp_bar()}')

  elif mode == 1:
    print(f'\033[1m  {profile.username}\'s\033[0m profile')
    print()
  
  elif mode == 3:
    print('\033[1m  GOAL TRACKER \033[0m')

  elif mode == 4:
    print('\033[1m  SHOP \033[0m')
    print(f'💰 Coins: \033[1m{profile.coin}\033[0m')
  
  elif mode == 6:
    print('\033[1m  SETTINGS \033[0m')

  if profile.settings_quote == True:
    print(f'\033[3m {random.choice(quotes)}\033[0m')
  print()

# initialization
if profile.username == 'undefined':
  os.system('cls')
  profile.date_registered = time.strftime("%Y-%m-%d")

  typingPrint('Welcome to the world of Neuromatrix!')
  while profile.username == 'undefined':
    profile.username = input("What do you wish to be identified as?\n>>> ").strip()
  profile.save()
  typingPrint(f'Congrats {profile.username}! You\'ve now set up your profile.')
  typingPrint('You can now wander around to discover the world of Neuromatrix.')
  typingPrint('When you see a menu like this ...')
  print('[1] Profile\n[2] Quiz\n[3] Goal Tracker\n[4] Shop\n[5] Settings\n[0] Exit')
  typingPrint('... you can select an option by typing the number and pressing enter.')
  typingPrint('For instance, if you want to check your profile, type 1 and press enter.')
  typingPrint('If you want to exit, type 0 and press enter.')
  typingPrint(f'Get it? Let\'s get started!')
  input("\n\033[3mPress anything to continue... \033[0m")

# daily reset
if time.strftime("%Y-%m-%d") != profile.last_login:
  print('\n\033[1mDAILY REWARD\033[0m')
  profile.today_learning_time = 0
  profile.quests_claimed = False

  # streak processing
  yesterdayT = time.strftime("%Y-%m-%d", time.localtime(time.time()-86400))
  if yesterdayT == profile.last_login:
    profile.streak += 1
    print(f'Welcome back with your {profile.streak}-day streak!')
  else:
    profile.streak = 1
    print(f'Welcome back!')
    if profile.date_registered != time.strftime("%Y-%m-%d"):
      print(f'You\'ve broken your streak unfortunately, as your previous login is at {profile.last_login}')
  
  # daily reward
  print(f'You\'ve received \033[1m7,500 (+{profile.streak*750} streak bonus)\033[0m coins as your daily reward!')
  profile.addCoin(7500 + (profile.streak * 750))
  if profile.streak % 10 == 0 and profile.streak != 0:
    print(f'You\'ve received a bonus of \033[1m15,000\033[0m coins for your {profile.streak}-day streak!')
    profile.addCoin(15000)

  profile.last_login = time.strftime("%Y-%m-%d")
  profile.save()
  print("\033[3mEnter full mode for better experience by clicking \033[1m'Maximize Panel Size' \033[0m")
  input("\n\033[3mPress anything to continue... \033[0m")

while status != -1:
  display()
  print('[1] Profile')
  print('[2] Quiz')
  print('[3] Goal Tracker')
  print('[4] Shop')
  print('[5] Settings')
  print('[0] Exit')

  status = input(">>> ").strip()

  if status == '1':
    display(1)

    print(f'❤️  HP\t\t\t\t{hp_bar()}')

    print(f'📅 Registered Date\t\t\033[1m{profile.date_registered}\033[0m')

    hours = int(profile.total_learning_time // 3600)
    minutes = int((profile.total_learning_time % 3600) // 60)
    seconds = int(profile.total_learning_time % 60)
    print(f'⏳ Total Learning Time\t\t\033[1m{hours:02}h {minutes:02}m {seconds:02}s')
    print()
    print(f'🔰 Tier\t\t\t\t\033[1m{profile.tier_accolade}\033[0m')
    print(f'🔥 Daily Streak\t\t\t\033[1m{profile.streak}\033[0m')
    print(f'💰 Coins\t\t\t\033[1m{profile.coin}\033[0m')
    print(f'⚔️  Bosses Unlocked\t\t \033[1m{len(profile.boss_unlocked)}\033[0m')
    print('\t\t\t\t(', end='')
    for i in profile.boss_unlocked:
      print(f'\033[1m{i}\033[0m', end=', ' if i != profile.boss_unlocked[-1] else '')
    print(')')

    if profile.last_coinflip == time.strftime("%Y-%m-%d"):
      coinflipAvail = "unavailable"
    else:
      coinflipAvail = "available"

    print(f'🎰 Coinflip\t\t\t\033[1m{coinflipAvail}\033[0m')

    print()
    print(f'🛡️  Fatal Immunity\t\t \033[1m{profile.abilities["fatal_immunity"]}%\033[0m')
    print(f'💵 Reward Multi\t\t\t\033[1m{profile.abilities["reward_boost"]}%\033[0m')
    print(f'🎖️  Streak Master\t\t \033[1m{profile.abilities["streak_bonus"]}%\033[0m')
    print(f'⚕️  Refreshing Hit\t\t \033[1m{profile.abilities["heal_on_correct"]}\033[0m')
    print(f'🌱 Glory of Victory\t\t\033[1m{profile.abilities["heal_on_win"]}\033[0m')

    print()
    input("\033[3mPress anything to continue... \033[0m")

  elif status == '2':
    def displayActiveQuiz():
      active_quizzes = []

      for q in quiz:
        if not q["archived"]:
          active_quizzes.append(q)

      if not active_quizzes:
        print("No active quizzes found.")
      else:
        name_width = 45
        cat_width  = 25

        print("\033[1mActive quizzes\033[0m")
        header = f"{'id':>3}  {'name':<{name_width}} {'category':<{cat_width}} {'questions':>9}  {'attempts':>8}  {'last_reviewed'}"
        print(header)
        print("-" * len(header))
    
        for q in active_quizzes:
          qid = q['id']
          name = q['name']
          category = q['category']
          num_q = len(q['questions'])
          attempts = q['attempts']
          last_rev = q['last_reviewed'] or 'Never'

          # Trunc long fields
          if len(name) <= name_width:
            name_disp = name
          else:
            name_disp = name[:name_width-1] + '…'
          if len(category) <= cat_width:
            cat_disp = category
          else:
            cat_disp = category[:cat_width-1] + '…'
          print(f"{qid:>3}  {name_disp:<{name_width}} {cat_disp:<{cat_width}} {num_q:>9}  {attempts:>8}  {last_rev}")

    while True:
      display()
      print('\033[1mQUIZ\033[0m')
      print('[1] \033[1mSTART\033[0m a quiz')
      print('[2] \033[1mCREATE\033[0m a quiz')
      print('[3] \033[1mARCHIVE\033[0m a quiz')
      print('[4] \033[1mRESTORE\033[0m archived quizzes')
      print('[0] Return')
      option = input(">>> ").strip()

      if option == '1':
        display()
        print("\033[1mQUIZ GAME\033[0m")
        active_quizzes = []
        for q in quiz:
          if not q["archived"]:
            active_quizzes.append(q)
        
        if not active_quizzes:
          print("No active quizzes available, go and create one!")
          input("\033[3mPress anything to continue...\033[0m")
          break

        if profile.hp <= 0:
          print("You need at least 1 HP to start a quiz. Go to Shop > Potions to buy one.")
          input("\033[3mPress anything to continue... \033[0m")
          break
        
        displayActiveQuiz()
        try:
          selected_id = int(input("\nEnter the quiz ID to start >>> ").strip())
        except:
          print("Invalid input")
          input("\033[3mPress anything to continue... \033[0m")
          break

        # Quiz selection
        selected_quiz = None
        for q in active_quizzes:
          if q["id"] == selected_id:
            selected_quiz = q
            break
        
        if not selected_quiz:
          print("Quiz selected does not exist or archived")
          input("\033[3mPress anything to continue... \033[0m")
          break
        
        print()
        # Boss selection
        boss_stats = {
          "Tiffany": {"value": [10000, 15000], "attack": [10, 15]},
          "Samuel": {"value": [15000, 20000], "attack": [18, 20]},
          "Rex": {"value": [17500, 27000], "attack": [20, 25]},
          "Sigma": {"value": [22500, 32500], "attack": [22, 27]},
          "Sky": {"value": [30000, 50000], "attack": [23, 38]},
          "The Royal": {"value": [45000, 62500], "attack": [25, 40]},
          "The Void": {"value": [50, 100000], "attack": [35, 50]}
        }

        print(f"{'ID':<4}{'Name':<10}{'Value':<20}{'Attack':<15}")
        print("-" * 50)

        # boss menu
        for i in range(len(profile.boss_unlocked)):
          boss_name = profile.boss_unlocked[i]
          stats = boss_stats[boss_name]
          value_range = f"{stats['value'][0]}–{stats['value'][1]}"
          attack_range = f"{stats['attack'][0]}–{stats['attack'][1]}"
          print(f"[{i+1}] {boss_name:<10}{value_range:<20}{attack_range:<15}")
          
        # boss select
        try:
          boss_choice = int(input("\nChoose your boss >>> ").strip()) - 1
          selected_boss = profile.boss_unlocked[boss_choice]
        except:
          print("Invalid boss selection.")
          input("\033[3mPress anything to continue... \033[0m")
          break

        # retrieve stats
        boss = boss_stats[selected_boss]
        value_min, value_max = boss["value"]
        attack_min, attack_max = boss["attack"]
        value = random.randint(value_min, value_max)

        correct = 0
        streak = 0
        max_streak = 0
        total_questions = len(selected_quiz["questions"])

        for q in selected_quiz["questions"]:
          q["user_choice"] = -1

        for i in range(total_questions):
          q = selected_quiz["questions"][i]
          display()
          print(f"\033[1mQuestion {i+1}/{total_questions}\033[0m")
          print(q["question"])
          for option_id in range(len(q["options"])):
            print(f"[{option_id+1}] {q['options'][option_id]}")

          try:
            ans = int(input(">>> ").strip()) - 1
          except:
            ans = -1
          q["user_choice"] = ans

          if ans == q["answer"]:
            correct += 1
            streak += 1
            max_streak = max(max_streak, streak)
            print("\033[32mCorrect!\033[0m")

            # Heal on correct
            profile.heal(profile.abilities["heal_on_correct"])

            # Surprise reward
            if streak >= 3 and random.random() < 0.2:
              bonus = random.randint(500, 1000)
              profile.addCoin(bonus)
              print(f"\033[1m🎉 Surprise Streak Bonus: +{bonus} coins!\033[0m")
          else:
            streak = 0
            damage = random.randint(attack_min, attack_max)
            profile.hp -= damage
            print(f"\033[31mWrong! The correct answer is: {q['options'][q['answer']]}\nYou took {damage} damage.\033[0m")
            if profile.hp <= 0:
              print("\033[1m💀 Oops... You died! Quiz ended.\033[0m")
              time.sleep(0.5)
              break
          input("\033[3mPress enter to continue... \033[0m")
        
        # Report of incorrect answers
        incorrect_exist = False
        for i in range(total_questions):
          if selected_quiz["questions"][i]["user_choice"] != selected_quiz["questions"][i]["answer"]:
            incorrect_exist = True

        if incorrect_exist:
          print("\n\033[1mREVIEW OF INCORRECT ANSWERS\033[0m")
          for i in range(total_questions):
            q = selected_quiz["questions"][i]
            user_answer = q["user_choice"]
            if user_answer != q["answer"]:
              print(f"\n📋 Question {i+1}: {q['question']}")
              if 0 <= user_answer < len(q['options']):
                print(f"❌ Your answer: {q['options'][user_answer]}")
              else:
                print(f"❌ Your answer: (Invalid Answer)")
              print(f"✅ Correct answer: {q['options'][q['answer']]}")
          input('\033[3mPress enter to continue...\033[0m')

        # final reward
        accuracy = correct / total_questions
        reward = int(accuracy * value * (1 + profile.abilities["reward_boost"] / 100) * (1 / (selected_quiz["attempts"] + 1)))

        bonus = int(reward * (max_streak * profile.abilities["streak_bonus"] / 100))

        display()
        if profile.hp > 0:
          print(f"\n\033[1m🏆 You defeated {selected_boss}!\033[0m")
          profile.heal(profile.abilities["heal_on_win"])
        else:
          print(f"\n\033[1m☠️  You failed to defeat {selected_boss}.\033[0m")
        
        print(f"✅ Correct\t{correct}/{total_questions}")
        print(f"🎯 Accuracy\t{accuracy:.2%}")
        print(f"🎉 Streak\t{max_streak}")
        print(f"💰 Reward\t{reward} (+{bonus}) coins")
        
        profile.addCoin(reward+bonus)

        selected_quiz["attempts"] += 1
        selected_quiz["last_reviewed"] = time.strftime("%Y-%m-%d")
        profile.save()
        save_file(QUIZ_FILE, quiz)
        input("\033[3mPress anything to continue... \033[0m")
      
      elif option == '2':
        display()
        print("\033[1mCREATE QUIZ\033[0m")

        name = input("Quiz name:\t\t\t>>> ").strip()
        if len(name) == 0:
          print("Quiz name cannot be empty.")
          input("\033[3mPress anything to continue...\033[0m")
          continue

        category = input("Category:\t\t\t>>> ").strip()
        if len(category) == 0:
          category = "Uncategorised"

        while True:
          try:
            num_q = int(input("How many questions? (min 5)\t>>> ").strip())
            if num_q >= 5:
              break
            print("You must have at least 5 questions.")
          except ValueError:
            print("Please enter a valid number.")

        questions = []
        for i in range(1, num_q + 1):
          display()
          print(f"\033[1mQuestion {i}/{num_q}\033[0m")
          q_text = input("Enter question:\n>>> ").strip()
          if not q_text:
            print("Question cannot be empty.")
            break

          while True:
            try:
              num_opts = int(input("Number of choices (2–4)?\n>>> ").strip())
              if 2 <= num_opts <= 4:
                break
              print("Please enter between 2 and 4 choices.")
            except ValueError:
              print("Please enter a valid number.")

          options = []
          for opt_i in range(1, num_opts + 1):
            opt = input(f"Option {opt_i}:\n>>> ").strip()
            options.append(opt)

          # Correct answer
          while True:
            ans = input(f"Which option is correct? (1–{num_opts})\n>>> ").strip()
            if ans.isdigit() and 1 <= int(ans) <= num_opts:
              answer_index = int(ans) - 1
              break
            print("Invalid choice.")

          questions.append({
            "question": q_text,
            "options": options,
            "answer": answer_index
          })

        new_quiz = {
          "id": len(quiz) + 1,
          "name": name,
          "category": category,
          "questions": questions,
          "archived": False,
          "created_by": profile.username,
          "created_at": time.strftime("%Y-%m-%d"),
          "last_reviewed": None,
          "attempts": 0
        }

        quiz.append(new_quiz)
        save_file(QUIZ_FILE, quiz)
        print(f"Quiz '{name}' created successfully with {len(questions)} questions.")
        input("\033[3mPress anything to continue...\033[0m")

      elif option == '3':
        display()
        print('\033[1mARCHIVE A QUIZ\033[0m')

        active_quizzes = []
        for q in quiz:
          if not q["archived"]:
            active_quizzes.append(q)

        if not active_quizzes:
          print("There are no active quizzes.")
          input("\033[3mPress anything to continue... \033[0m")
          continue

        displayActiveQuiz()
        try:
          sel = int(input("\nEnter the quiz ID to archive >>> ").strip())
        except:
          print("Invalid input.")
          input("\033[3mPress anything to continue... \033[0m")
          continue

        selected = None
        for q in active_quizzes:
          if q["id"] == sel:
            selected = q
            break

        if not selected:
          print("Invalid quiz ID.")
          input("\033[3mPress anything to continue... \033[0m")
          continue

        selected["archived"] = True
        save_file(QUIZ_FILE, quiz)

        print(f"Quiz \033[1m{selected['name']}\033[0m archived.")
        input("\033[3mPress anything to continue... \033[0m")

      elif option == '4':
        display()
        archived_quizzes = []

        for q in quiz:
          if  q["archived"]:
            archived_quizzes.append(q)

        if not archived_quizzes:
          print("No archived quizzes found.")
        else:
          name_width = 26
          cat_width  = 16

          print("\033[1mArchived quizzes\033[0m")
          header = f"{'id':>3}  {'name':<{name_width}} {'category':<{cat_width}} {'questions':>9}  {'attempts':>8}  {'last_reviewed'}"
          print(header)
          print("-" * len(header))

          for q in archived_quizzes:
            qid = q['id']
            name = q['name']
            category = q['category']
            num_q = len(q['questions'])
            attempts = q['attempts']
            last_rev = q['last_reviewed'] or 'Never'

            # Trunc long fields
            if len(name) <= name_width:
              name_disp = name
            else:
              name_disp = name[:name_width-1] + '…'
            if len(category) <= cat_width:
              cat_disp = category
            else:
              cat_disp = category[:cat_width-1] + '…'
            print(f"{qid:>3}  {name_disp:<{name_width}} {cat_disp:<{cat_width}} {num_q:>9}  {attempts:>8}  {last_rev}")

            try:
              sel = int(input("\nEnter the quiz ID to restore >>> ").strip())
            except:
              print("Invalid input.")
              input("\033[3mPress anything to continue... \033[0m")
              continue

            selected = False
            for q in archived_quizzes:
              if q["id"] == sel:
                selected = q
                break

            if not selected:
              print("Invalid quiz ID.")
              input("\033[3mPress anything to continue... \033[0m")
              continue

            selected["archived"] = False
            save_file(QUIZ_FILE, quiz)

            print(f"Quiz \033[1m{selected['name']}\033[0m restored.")

        print()

        input("\033[3mPress anything to continue... \033[0m")

      elif option == '0':
        break
  
  elif status == '3':
    while True:
      def displayActiveGoal():
        display(3)
        for g in goal:
          if g['end_date'] == "undefined":
            checkpoints_total = len(g["checkpoints"])
            checkpoints_claimed = 0
            for i in g["checkpoints"]:
              if i:
                checkpoints_claimed += 1
            
            portion = (g["deposit"] * 2) // ((len(g["checkpoints"]) + 1))
            claimed_coins = checkpoints_claimed * portion
            
            last_claimed = "None"
            next_claim_coins = portion
            for date in reversed(g["checkpoints"]):
              if date:
                last_claimed = date
                break
            
            # final reward doubled
            if checkpoints_claimed == checkpoints_total - 1:
              next_claim_coins += portion 
            
            if time.strftime("%Y-%m-%d") == last_claimed:
              claim_status = "\033[31munavailable\033[0m"
            else:
              claim_status = f"\033[32mavailable\033[0m (+{next_claim_coins} coins)"

            print(f'[{g["id"]}] \033[1m{g["name"]}\033[0m')
            print(f'⤷  Description\t\t{g["description"]}')
            print(f'⤷  Start Date\t\t{g["start_date"]}')
            print(f'⤷  Checkpoints\t\t{checkpoints_claimed} / {checkpoints_total}')
            print(f'⤷  Claimed Coins\t{claimed_coins} / {g["deposit"]*2}')
            print(f'⤷  Last Claimed\t\t{last_claimed} (claim {claim_status})')
            print()
      
      def goalTrackerIntro(mode='p'):
        if mode == 'p':
          typingPrint('A goal tracker is a way to set your goals (not necessarily in this game) and track your progress towards them.')
          print()
          typingPrint('You may deposit coins, and you can set the amount of checkpoints.')
          typingPrint('You can have a minimum of 1 checkpoint, with the maximum of 4 checkpoints.')
          print()
          typingPrint('After completing the checkpoints, you may get a sum of coins.')
          typingPrint('For every checkpoint you complete, you can claim a portion of the coins.')
          typingPrint('Completing the entire goal will be taken as completing two checkpoints.')
          typingPrint('The total amount of coins you can get is double the amount you deposited.')
          print()
          typingPrint('You may have at most 3 concurrent goals, with each having a maximum of 25,000 coins deposit.')
          typingPrint('If you want to end a goal early, you will be returned half of your deposit,')
          typingPrint('or the amount of claimed coins, whichever is higher.')
          input("\033[3mPress enter to continue ...\033[0m\n>>> ")
        else:
          print('A goal tracker is a way to set your goals (not necessarily in this game) and track your progress towards them.')
          print()
          print('You may deposit coins, and you can set the amount of checkpoints.')
          print('You can have a minimum of 1 checkpoint, with the maximum of 4 checkpoints.')
          print()
          print('After completing the checkpoints, you may get a sum of coins.')
          print('For every checkpoint you complete, you can claim a portion of the coins.')
          print('Completing the entire goal will be taken as completing two checkpoints.')
          print('The total amount of coins you can get is double the amount you deposited.')
          print()
          print('You may have at most 3 concurrent goals, with each having a maximum of 25,000 coins deposit.')
          print('If you want to end a goal early, you will be returned half of your deposit,')
          print('or the amount of claimed coins, whichever is higher.')
          input("\033[3mPress enter to continue ...\033[0m\n>>> ")


      displayActiveGoal()
      
      print('[1] \033[1mCREATE\033[0m a new goal')
      print('[2] \033[1mCLAIM\033[0m a checkpoint')
      print('[3] \033[1mEND\033[0m a goal early')
      print('[4] \033[1mVIEW\033[0m archived goals')
      print('[5] \033[1mLEARN\033[0m about goal tracker')
      print('[0] Return')
      option = input(">>> ").strip()

      if option == '1':
        activeGoal = sum(1 for g in goal if g['end_date'] == "undefined")
        if not goal:
          goalTrackerIntro('allatonce')
        
        while True:
          if activeGoal >= 3:
            display(3)
            print('You can only have a maximum of 3 concurrent goals.')
            print('Please end a goal before creating a new one.')
            input("\033[3mPress anything to continue... \033[0m")
            break

          display(3)
          try:
            print('\033[1m< CREATING A NEW GOAL >\033[0m')
            name = input("Enter the \033[1mname\033[0m of your goal\n>>> ").strip()
            print("\nEnter the \033[1mdescription\033[0m of your goal.\nFor instance, what each of your checkpoints represents.")
            description = input(">>> ").strip()
            start_date = time.strftime("%Y-%m-%d")
            while True:
              print("\nEnter the \033[1mamount of checkpoints\033[0m of your goal.")
              print("It can be 1 to 4 checkpoints.")
              print("The amount of reward per checkpoint is split evenly.")
              print("Completing the goal is taken as 2 checkpoints.")
              checkpoints = int(input(">>> ").strip())
              if checkpoints >= 1 and checkpoints <= 4:
                break
              print("You must enter a valid number of checkpoints (1-4).")
              input("\033[3mPress anything to continue... \033[0m")
            print("\nEnter the \033[1mdeposit\033[0m of your goal. The maximum deposit is 25,000 coins.")
            print("You will receive double your deposit if you complete the goal.")
            while True:
              deposit = int(input(">>> ").strip())
              if deposit > 0 and deposit <= 25000 and deposit <= profile.coin:
                break
              print("You must enter a deposit between 1 and 25,000 coins, and have enough coins to create the goal.")
              input("\033[3mPress anything to continue... \033[0m")
          except:
            print("Error: Invalid input. Please try again.")
            input("\033[3mPress anything to continue... \033[0m")
            break
            
          newGoal = {
            "id": len(goal) + 1,
            "name": name,
            "description": description,
            "start_date": start_date,
            "end_date": "undefined",
            "deposit": int(deposit),
            "checkpoints": [""] * int(checkpoints)
          }
          
          display(3)
          print(f'\nYou are about to create the following goal:')
          print(f'Name\t\t\t\033[1m{newGoal["name"]}\033[0m')
          print(f'Description\t\t\033[1m{newGoal["description"]}\033[0m')
          print(f'Start Date\t\t\033[1m{newGoal["start_date"]}\033[0m')
          print(f'Deposit\t\t\t\033[1m{newGoal["deposit"]}\033[0m')
          print(f'Checkpoints\t\t\033[1m{len(newGoal["checkpoints"])}\033[0m')
          confirm = input("Is this correct? (y/n) \n>>> ").strip().lower()
          if confirm == 'y':
            profile.addCoin(-newGoal['deposit'])
            goal.append(newGoal)
            save_file(GOAL_FILE, goal)
            print(f'Goal \033[1m{newGoal["name"]}\033[0m has been created successfully!')
            input("\033[3mPress anything to continue... \033[0m")
            break
          else:
            print('Goal creation cancelled.')
            input("\033[3mPress anything to continue... \033[0m")
            break

      elif option == '2':
        display(3)
        claimable_goals = []
        for g in goal:
          if g['end_date'] == "undefined":
            last_claimed = None
            for date in reversed(g["checkpoints"]):
              if date:
                last_claimed = date
                break
            if last_claimed != time.strftime("%Y-%m-%d"):
              claimable_goals.append(g)

        if not claimable_goals:
          print("No goals available for claim today.")
          input("\033[3mPress anything to continue... \033[0m")
          continue
        
        # display goals available for claim
        for g in claimable_goals:
          checkpoints_total = len(g["checkpoints"])
          checkpoints_claimed = sum(1 for i in g["checkpoints"] if i)
          portion = (g["deposit"] * 2) // (checkpoints_total + 1)
          next_claim_coins = portion
          if checkpoints_claimed == checkpoints_total - 1:
            #completing checkpoint => double reward
            next_claim_coins += portion 
          print(f'[{g["id"]}] \033[1m{g["name"]}\033[0m')
          print(f'{checkpoints_claimed} / {checkpoints_total} checkpoints claimed, next claim: +{next_claim_coins} coins')
          print()

        try:
          selected_id = int(input("Enter the goal ID you want to claim >>> ").strip())
        except:
          print("Invalid input.")
          input("\033[3mPress anything to continue... \033[0m")
          continue

        selected_goal = None
        for g in claimable_goals:
          if g["id"] == selected_id:
            selected_goal = g
            break

        if not selected_goal:
          print("Goal ID not found or not available for claim.")
          input("\033[3mPress anything to continue... \033[0m")
          continue

        # Claim the next available checkpoint
        for i in range(len(selected_goal["checkpoints"])):
          if not selected_goal["checkpoints"][i]:
            selected_goal["checkpoints"][i] = time.strftime("%Y-%m-%d")
            break

        checkpoints_total = len(selected_goal["checkpoints"])
        checkpoints_claimed = sum(1 for i in selected_goal["checkpoints"] if i)
        portion = (selected_goal["deposit"] * 2) // (checkpoints_total + 1)
        reward = portion

        # final reward, complete goal
        print()
        if checkpoints_claimed == checkpoints_total:
          reward += portion
          selected_goal["end_date"] = time.strftime("%Y-%m-%d")
          print(f"Congratulations!\nYou have completed your goal and claimed \033[1m{reward} coins\033[0m!")
        else:
          print(f"Checkpoint reward: \033[1m{reward} coins\033[0m claimed!")

        profile.addCoin(reward)
        save_file(GOAL_FILE, goal)
        input("\033[3mPress anything to continue... \033[0m")

      elif option == '3':
        display(3)
        displayActiveGoal()
        active_goals = []
        for g in goal:
          if g['end_date'] == "undefined":
            active_goals.append(g)
        
        try:
          end_goal_id = int(input("Enter the goal ID you wish to end early >>> ").strip())
        except:
          print("Invalid input. Please enter a valid goal ID.")
          input("\033[3mPress anything to continue... \033[0m")
          continue
        
        selected_goal = None
        for g in active_goals:
          if g['id'] == end_goal_id:
            selected_goal = g
            break

        if not selected_goal:
          print("Invalid input. Please enter the ID of an active goal")
          input("\033[3mPress anything to continue... \033[0m")
          continue

        checkpoints_total = len(selected_goal["checkpoints"])
        checkpoints_claimed = sum(1 for i in selected_goal["checkpoints"] if i)
        portion = (selected_goal["deposit"] * 2) // (checkpoints_total + 1)
        claimed_coins = checkpoints_claimed * portion
        half_deposit = selected_goal["deposit"] // 2

        # refund
        if half_deposit > claimed_coins:
          refund = half_deposit - claimed_coins
          profile.addCoin(refund)
          print(f"\nGoal \033[1m{selected_goal['name']}\033[0m ended early.")
          print(f"You received \033[1m{refund} coins\033[0m refund (deposit / 2 - already claimed coins).")
        else:
          refund = 0
          print(f"\nGoal \033[1m{selected_goal['name']}\033[0m ended early.")
          print(f"You have already claimed more than half your deposit, so no additional coins are refunded.")

        selected_goal["end_date"] = time.strftime("%Y-%m-%d")
        profile.save()
        save_file(GOAL_FILE, goal)
        input("\033[3mPress anything to continue... \033[0m")

      elif option == '4':
        display(3)
        for g in goal:
          if g['end_date'] != "undefined":
            checkpoints_total = len(g["checkpoints"])
            checkpoints_claimed = 0
            for i in g["checkpoints"]:
              if i:
                checkpoints_claimed += 1
            
            portion = (g["deposit"] * 2) // ((len(g["checkpoints"]) + 1))
            claimed_coins = checkpoints_claimed * portion
            if checkpoints_claimed == checkpoints_total:
              claimed_coins = g['deposit'] * 2
            
            if claimed_coins == g['deposit'] * 2:
              claim_color = "\033[32m"
            elif claimed_coins >= g['deposit']:
              claim_color = "\033[33m"
            else:
              claim_color = "\033[31m"

            # early-ended goal refund
            if claimed_coins < g['deposit']//2:
              claimed_coins = g['deposit']//2

            print(f'[{g["id"]}] \033[1m{g["name"]}\033[0m')
            print(f'⤷  Description\t\t{g["description"]}')
            print(f'⤷  Period\t\t{g["start_date"]} to {g["end_date"]}')
            print(f'⤷  Claimed Coins\t{claim_color}{claimed_coins}\033[0m/{g["deposit"]*2}')
            print(f'⤷  Checkpoints\t\t{checkpoints_claimed}/{checkpoints_total}')
            print()
        input("\033[3mPress anything to continue... \033[0m")
      
      elif option == '5':
        display(3)
        goalTrackerIntro()
      
      elif option == '0':
        break
      
  elif status == '4':
    while True:
      display(4)
      print('[1] Coinflip')
      print('[2] Tier Upgrading')
      print('[3] Potions')
      print('[4] Abilities')
      print('[5] Bosses')
      print('[6] Mercy Potion')
      print('[0] Return')
      option = input(">>> ").strip()
      if option == '1':
        if profile.tier_accolade == 'None':
          print('You need to be higher or equal to Bronze tier to use this feature.')
          input('\033[3mPress anything to continue... \033[0m')
          break
        
        if profile.last_coinflip == time.strftime("%Y-%m-%d"):
          print('You have already played coinflip today.')
          input('\033[3mPress anything to continue... \033[0m')
          break
        
        if profile.coin < 5000:
          print('You need at least 5,000 coins to play coinflip.')
          input('\033[3mPress anything to continue... \033[0m')
          break

        if profile.last_coinflip == 'undefined':
          print('Coinflip is a game which you choose heads or tails, and have a 45% chance of doubling your bet')

        bet = int(input('Please enter your bet (5,000 - 25,000 coins): '))
        input('Choose HEADS or TAILS\n>>> ')

        if bet < 5000 or bet > 25000:
          print('Invalid bet amount. Please try again.')
          input('\033[3mPress anything to continue... \033[0m')
          break
        elif bet > profile.coin:
          print('You cannot bet more than what you have.')
          input('\033[3mPress anything to continue... \033[0m')
          break

        if random.random() <= 0.45:
          profile.addCoin(bet)
          profile.last_coinflip = time.strftime("%Y-%m-%d")
          print(f'Congratulations, you WON {bet} coins and now have {profile.coin} coins.')
        else:
          profile.addCoin(-bet)
          profile.last_coinflip = time.strftime("%Y-%m-%d")
          print(f'You LOST {bet} coins and now have {profile.coin} coins.')
        profile.save()
        input('\033[3mPress anything to continue... \033[0m')
        break

      elif option == '2':
        tierList = ['None', 'Bronze', 'Silver', 'Golden', 'Platinum', 'Diamond', 'Amethyst', 'Sapphire', 'Emerald']
        tierCost = [0, 25000, 100000, 250000, 500000, 1000000, 2500000, 5000000, 7000000]

        userTierIndex = tierList.index(profile.tier_accolade)

        if profile.coin >= tierCost[userTierIndex + 1]:
          affordableColor = '\033[32m'
        else:
          affordableColor = '\033[31m'

        for i in range(userTierIndex+1, len(tierList)):
          if i == userTierIndex + 1:
            print(f'NEXT:\t{tierList[i]:<10}\t{affordableColor}{tierCost[i]:>9} coins\033[0m')
          else:
            print(f'\t{tierList[i]:<10}\t{tierCost[i]:>9} coins')

        if affordableColor == '\033[32m':
          ans = input('Do you wish to upgrade to the next tier? [y/n]\n>>> ')
          if ans.lower() == 'y':
            profile.addCoin(-tierCost[userTierIndex + 1])
            profile.tier_accolade = tierList[userTierIndex + 1]
            print(f'Congratulations, you have been upgraded to \033[1m{profile.tier_accolade}\033[0m tier!')
        input('\033[3mPress anything to continue... \033[0m')
        break

      elif option == '3':
        print(f'❤️   HP:  {hp_bar()}')
        if profile.hp < profile.max_hp:
          print()
          print('\033[1m[1] Healing Potion\t5,000 coins\033[0m')
          print('\033[3mRecover 25 HP or to maximum capacity.\033[0m')
          print()
          print('\033[1m[2] Recovery Potion\t25,000 coins\033[0m')
          print('\033[3mRecover HP to maximum capacity.\033[0m')

          ans = input(">>> ").strip()
          hpOriginal = profile.hp
          if ans == '1':
            if profile.coin < 5000:
              print('You need at least 5,000 coins to use a Healing Potion.\nGo to Shop > Mercy Potion for free healing.')
              input('\033[3mPress anything to continue... \033[0m')
              break
            profile.addCoin(-5000)
            profile.heal(25)
          elif ans == '2':
            if profile.coin < 25000:
              print('You need at least 25,000 coins to use a Recovery Potion.')
              input('\033[3mPress anything to continue... \033[0m')
              break
            profile.addCoin(-25000)
            profile.heal(profile.max_hp - profile.hp)
          else:
            print('Invalid option, please try again.')
          if profile.hp > hpOriginal:
            print(f'You have \033[32mhealed\033[0m \033[1m{profile.hp - hpOriginal}\033[0m HP and you now have \033[1m{profile.hp}\033[0m HP.')
        else:
          print('\033[0mYour HP bar is full.')

        input('\033[3mPress anything to continue... \033[0m')
        break

      elif option == '4':
        while True:
          abilities = [
            {
              "name": "Strengthened Strength",
              "effect": "max_hp",
              "description": "Increases HP capacity to n",
              "tiers": [
                {"value": 110, "cost": 15000, "required_tier": "Bronze"},
                {"value": 115, "cost": 20000, "required_tier": "Silver"},
                {"value": 120, "cost": 50000, "required_tier": "Golden"},
                {"value": 130, "cost": 100000, "required_tier": "Platinum"},
                {"value": 140, "cost": 250000, "required_tier": "Diamond"},
                {"value": 150, "cost": 500000, "required_tier": "Amethyst"},
                {"value": 175, "cost": 1000000, "required_tier": "Sapphire"},
                {"value": 200, "cost": 2000000, "required_tier": "Emerald"}
              ]
            },
            {
              "name": "Critical Immunity",
              "effect": "fatal_immunity",
              "description": "n% to avoid fatal damage once",
              "tiers": [
                {"value": 50, "cost": 150000, "required_tier": "Platinum"},
                {"value": 60, "cost": 300000, "required_tier": "Diamond"},
                {"value": 65, "cost": 675000, "required_tier": "Amethyst"},
                {"value": 75, "cost": 1200000, "required_tier": "Sapphire"},
                {"value": 100, "cost": 2000000, "required_tier": "Emerald"}
              ]
            },
            {
              "name": "Reward Multiplier",
              "effect": "reward_boost",
              "description": "Increases coin reward by n%",
              "tiers": [
                {"value": 20, "cost": 20000, "required_tier": "Bronze"},
                {"value": 35, "cost": 45000, "required_tier": "Silver"},
                {"value": 50, "cost": 75000, "required_tier": "Golden"},
                {"value": 75, "cost": 150000, "required_tier": "Platinum"},
                {"value": 100, "cost": 300000, "required_tier": "Diamond"},
                {"value": 125, "cost": 600000, "required_tier": "Amethyst"},
                {"value": 150, "cost": 1150000, "required_tier": "Sapphire"},
                {"value": 200, "cost": 2200000, "required_tier": "Emerald"}
              ]
            },
            {
              "name": "Streak Master",
              "effect": "streak_bonus",
              "description": "Adds (highest streak * n)% to coin reward",
              "tiers": [
                {"value": 1.5, "cost": 20000, "required_tier": "Bronze"},
                {"value": 1.75, "cost": 45000, "required_tier": "Silver"},
                {"value": 2, "cost": 75000, "required_tier": "Golden"},
                {"value": 2.25, "cost": 150000, "required_tier": "Platinum"},
                {"value": 2.5, "cost": 250000, "required_tier": "Diamond"},
                {"value": 2.75, "cost": 500000, "required_tier": "Amethyst"},
                {"value": 3, "cost": 1150000, "required_tier": "Sapphire"},
                {"value": 3.25, "cost": 2200000, "required_tier": "Emerald"}
              ]
            },
            {
              "name": "Refreshing Hit",
              "effect": "heal_on_correct",
              "description": "Heals HP by n on correct answer",
              "tiers": [
                {"value": 5, "cost": 200000, "required_tier": "Platinum"},
                {"value": 7, "cost": 320000, "required_tier": "Diamond"},
                {"value": 10, "cost": 600000, "required_tier": "Amethyst"},
                {"value": 13, "cost": 1150000, "required_tier": "Sapphire"},
                {"value": 15, "cost": 2200000, "required_tier": "Emerald"}
              ]
            },
            {
              "name": "Glory of Victory",
              "effect": "heal_on_win",
              "description": "Heals HP by n when winning",
              "tiers": [
                {"value": 12, "cost": 20000, "required_tier": "Bronze"},
                {"value": 15, "cost": 45000, "required_tier": "Silver"},
                {"value": 19, "cost": 75000, "required_tier": "Golden"},
                {"value": 25, "cost": 250000, "required_tier": "Platinum"},
                {"value": 30, "cost": 320000, "required_tier": "Diamond"},
                {"value": 36, "cost": 600000, "required_tier": "Amethyst"},
                {"value": 43, "cost": 1150000, "required_tier": "Sapphire"},
                {"value": 55, "cost": 2200000, "required_tier": "Emerald"}
              ]
            }
            ]
          
          display(4)
          print('\033[1mUPGRADING ABILITIES\033[0m')

          tierList = ['None', 'Bronze', 'Silver', 'Golden', 'Platinum', 'Diamond', 'Amethyst', 'Sapphire', 'Emerald']
          player_tierID = tierList.index(profile.tier_accolade)

          print(f"{'id':>3}  {'name':<22} {'description':<45} {'n':^11}  {'cost':>9}  {'tier':<10}")
          print("-" * 115)

          available_upgrades = []
          ability_id = 1

          for ability in abilities:
            key = ability["effect"]
            if key == "max_hp":
              current_value = profile.max_hp
            else:
              current_value = profile.abilities[key]
            
            next_tier = None
            for tier in ability["tiers"]:
              if tier["value"] > current_value:
                next_tier = tier
                break

            required_tierID = tierList.index(next_tier["required_tier"])
            cost = next_tier["cost"]
            new_value = next_tier["value"]
            
            if profile.coin >= cost:
              price_col = "\033[32m"
            else:
              price_col = "\033[31m"
              
            if player_tierID < required_tierID:
              lock_icon = "🔒"
            else:
              lock_icon = ""

            available_upgrades.append({
              "id": ability_id,
              "name": ability["name"],
              "description": ability["description"],
              "current_value": current_value,
              "new_value": new_value,
              "cost": cost,
              "lock_icon": lock_icon,
              "key": key,
              "required_tier": next_tier["required_tier"]
            })

            print(f"{ability_id:>3}  {ability['name']:<22} {ability['description']:<45} {current_value:>4} → {new_value:<4}  {price_col}{cost:>9}\033[0m  {next_tier['required_tier']:<10} {lock_icon}")
            ability_id += 1

          if not available_upgrades:
            print("\nAll abilities are maxed out!")
            input("\033[3mPress anything to continue... \033[0m")
            break

          try:
            choice = input("\nEnter ability ID to upgrade (or 0 to return):\n>>> ").strip()
            selected_id = int(choice)
          except ValueError:
            print("Invalid ability ID")
            input("\033[3mPress anything to continue... \033[0m") 
            break

          if selected_id == 0:
            break

          selected = None
          for upgrade in available_upgrades:
            if upgrade["id"] == selected_id:
              selected = upgrade
              break

          if not selected:
            print("Invalid ability ID")
            input("\033[3mPress anything to continue... \033[0m")
            break

          required_tierID = tierList.index(selected["required_tier"])

          if player_tierID < required_tierID:
            print(f"You need the {selected['required_tier']} tier to upgrade this ability.")
          elif profile.coin < selected["cost"]:
            print("Not enough coins.")
          else:
            profile.addCoin(-selected["cost"])
            profile.upgrade_ability(selected["key"], selected["new_value"])
            profile.save()
            print(f"\nYou upgraded \033[1m{selected['name']}\033[0m to {selected['new_value']}!")

          input("\033[3mPress anything to continue... \033[0m")

      elif option == '5':
        display(4)
        print('\033[1mBOSSES SHOP\033[0m')
        bossName = ["Tiffany", "Samuel", "Rex", "Sigma", "Sky", "The Royal", "The Void"]
        unlockCriteria = ["None", "Silver", "Platinum", "Diamond", "Amethyst", "Sapphire", "Emerald"]

        valueMin = [10000, 15000, 17500, 22500, 30000, 45000, 50]
        valueMax = [15000, 20000, 27000, 32500, 50000, 62500, 100000]

        attackMin = [10, 18, 20, 22, 23, 25, 35]
        attackMax = [15, 20, 25, 27, 38, 40, 50]

        cost = [0, 35000, 125000, 350000, 750000, 1250000, 2500000]

        tierList = ['None', 'Bronze', 'Silver', 'Golden', 'Platinum', 'Diamond', 'Amethyst', 'Sapphire', 'Emerald']
        player_tierID = tierList.index(profile.tier_accolade)

        header = f"{'id':>3}  {'name':<14} {'unlock':<10} {'value':>13}  {'attack':>11}  {'cost':>8}"
        print(header)
        print("-" * len(header))

        for i in range(len(bossName)):
          name = bossName[i]
          unlock_req = unlockCriteria[i]
          req_rankID = tierList.index(unlock_req)
          value_str = f"{valueMin[i]}-{valueMax[i]}"
          attack_str = f"{attackMin[i]}-{attackMax[i]}"
          boss_cost = cost[i]
          price_col = "\033[32m" if profile.coin >= boss_cost else "\033[31m"

          if player_tierID < req_rankID:
            lock_icon = "🔒"
          else:
            lock_icon = ""
          
          if name not in profile.boss_unlocked:
            print(f"{i+1:>3}  {name:<14} {unlock_req:<10} {value_str:>13}  {attack_str:>11}  {price_col}{boss_cost:>8}\033[0m  {lock_icon}")

        choice = input("\nEnter boss ID to unlock:\n>>> ").strip()
        if not choice.isdigit():
          print("Invalid input")
          input("\033[3mPress anything to continue... \033[0m")
          break
        boss_id = int(choice)
        
        if boss_id < 1 or boss_id > len(bossName):
          print("Boss ID out of range")
          input("\033[3mPress anything to continue... \033[0m")
          break

        name        = bossName[boss_id-1]
        unlock_req  = unlockCriteria[boss_id-1]
        req_rankID  = tierList.index(unlock_req)
        boss_cost   = cost[boss_id-1]

        if name in profile.boss_unlocked:
          print("Boss already unlocked")
        elif player_tierID < req_rankID:
          print(f"You need the {unlock_req} tier to unlock this boss")
        elif profile.coin < boss_cost:
          print("Not enough coins")
        else:
          print(f"You have unlocked \033[1m{name}\033[0m.")
          profile.addCoin(-boss_cost)
          profile.boss_unlocked.append(name)
          profile.save()
        input("\033[3mPress anything to continue... \033[0m")
        break

      elif option == '6':
        if profile.coin >= 5000 or profile.hp >= 1:
          print('You do not need to use a Mercy Potion right now.')
          input('\033[3mPress anything to continue... \033[0m')
          break
        else:
          hpOriginal = profile.hp
          profile.hp += 20
          print(f'You have \033[32mhealed\033[0m \033[1m{profile.hp - hpOriginal}\033[0m HP and you now have \033[1m{profile.hp}\033[0m HP.')
          profile.save()
          input("\033[3mPress anything to continue... \033[0m")
          break

      elif option == '0':
        break

      else:
        print('Invalid option, please try again.')
        break
  
  elif status == '5':
    display(6)
    print('id\tSettings\t\t\tCurrent Value\033[0m')
    print(f'1\tShow Quotes\t\t\t\033[1m{profile.settings_quote}\033[0m')
    print()
    option = input("Enter the settings id you wish to toggle >>> ").strip()
    if option == '1':
      if profile.settings_quote == True:
        profile.settings_quote = False
        display(6)
        print('Quotes are now turned off.')
      else:
        profile.settings_quote = True
        display(6)
        print('Quotes are now turned on.')
      profile.save()
      input("\033[3mPress anything to continue... \033[0m")
    else:
      print('Invalid option, please try again.')
      input("\033[3mPress anything to continue... \033[0m")
  
  elif status == '0':
    status = -1
    os.system('cls')
    print('Exiting...')
    time.sleep(0.2)
    os.system('cls')
    break

profile.today_learning_time += elapsed_time("l")
profile.total_learning_time += elapsed_time("l")
profile.save()
save_file(GOAL_FILE, goal)
save_file(QUEST_FILE, quest)
save_file(QUIZ_FILE, quiz)

verbList = ['studied', 'worked', 'practiced', 'refined']
print(f"Nice work {profile.username}, you've {random.choice(verbList)} for ...")
print(f"- \033[1m{elapsed_time('d')}\033[0m in this session and,")

hours = int(profile.today_learning_time // 3600)
minutes = int((profile.today_learning_time % 3600) // 60)
seconds = int(profile.today_learning_time % 60)
print(f"- \033[1m{hours:02}h {minutes:02}m {seconds:02}s\033[0m today.")
print('\nSee you next time!')