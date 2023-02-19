# introduction
def introduction():
  print(
    "Welcome to Eggi. This program is designed to help you make sense of your symptoms. 57% of women are misdiagnosed by healthcare professionals. Please enter your symptoms and we will do our best to properly diagnose you. Thank you and we hope you feel better."
  )
  print("Type y for yes and n for no.")


# disorders
symovarian_cyst = [
  "pelvic pain", "painful intercourse", "painful bowel movements",
  "low fertility", "small appetite", "frequent bowel movements"
]
symmenopause = [
  "irregular periods", "vaginal dryness", "hot flashes", "chills",
  "night sweats", "sleep problems", "mood changes", "weight gain",
  "slowed metabolism", "thinning of hair", "decreasing breast size"
]
sympcos = [
  "irregular periods", "deepening of voice", "increased muscle mass",
  "balding", "excess body hair"
]
symendometriosis = [
  "abdominal pain", "back pain", "heavy bleeding",
  "bleeding during intercourse", "painful bowel movements"
]
sympolyops = [
  "heavy bleeding", "bleeding during intercourse", "white or yellow discharge",
  "spotting between period"
]

# disorders list
disorders = [
  symovarian_cyst, symmenopause, sympcos, symendometriosis, sympolyops
]

# symptoms list
symptoms = dict()
symNames = [
  "pelvic pain", "white or yellow discharge", "excess body hair",
  "painful bowel movements", "painful intercourse", "irregular periods",
  "hot flashes", "vaginal dryness", "chills", "night sweats", "sleep problems",
  "mood changes", "weight gain", "slowed metabolism", "thinning of hair",
  "dry skin", "decreasing breast size", "abdominal pain", "heavy bleeding",
  "spotting between period", "deepening of voice", "increased muscle mass",
  "balding", "bleeding during intercourse", "small appetite", "low fertility",
  "frequent bowel movements", "back pain"
]

# lists for medications
birth_control = ""
thyroid_medicine = ""
anti_depressants = ""
medications_display = ["birth control", "thyroid medicine", "anti-depressants"]
medications_code = [birth_control, thyroid_medicine, anti_depressants]


# ask age
def ask_age():
  ask_age.age = int(input("\nPlease input your age: "))


# ask height
def ask_height():
  ask_height.height = int(input("\nPlease input your height (inches): "))


# ask first period
def ask_first_period():
  ask_first_period.first_period = int(
    input("\nHow old were you when you got your first period?: "))


# ask medications
def ask_medications():
  print("\n", medications_display)
  ask_medications.medications = input(
    "Are you on any of the listed medications? ")
  if ask_medications.medications == "y":
    ask_medications.birth_control = input("\nAre you on birth control? ")
    ask_medications.thyroid_medicine = input("\nAre you on thyroid medicine? ")
    ask_medications.anti_depressants = input("\nAre you on anti-depressants? ")


# ask common symptoms
def ask_symptoms():
  print(
    "\nWhich of the following symptoms are you experiencing? \ntype n for no or y for yes"
  )
  for sym in symNames:
    user = input(f"\nHave you experienced {sym} in the past 60 days?\n")
    if (user.lower() == "n"):
      user = 0
    else:
      user = 1
    symptoms[sym] = user


# check menopause
def check_menopause():
  if ask_age.age >= 45 and ask_age.age <= 69:
    s = 0
    for sym in symmenopause:
      s += symptoms[sym]
    if len(symmenopause) / 2 <= s:
      print(
        "\nYou may be going through menopause. Menopause is a natural decline in the reproductive hormones that occur during your 40s to 50s, which causes for your period to not occur anymore. "
      )
    else:
      print(
        "\nYou may experience menopause soon because you are in the age range for it. "
      )


# check first period range irregularities
def check_first_period_irregularities():
  if (ask_age.age - ask_first_period.first_period) <= 2:
    print(
      "\nYou may have some symptoms because your period is not regular yet.")


# check medications
def check_medications():
  if ask_medications.medications == "y":
    if ask_medications.birth_control == "y":
      print(
        "You may be experiencing some symptoms because you are on birth control."
      )
    if ask_medications.thyroid_medicine == "y":
      print(
        "You may be experiencing some symptoms because you are on thyroid medicine."
      )
    if ask_medications.anti_depressants == "y":
      print(
        "You may be experiencing some symptoms because you are on anti-depressants."
      )


# check ovarian cyst
def check_ovarian_cyst():
  s = 0
  for sym in symovarian_cyst:
    s += symptoms[sym]
  if len(symovarian_cyst) / 2 <= s:
    print(
      "\nYou may be at risk for ovarian cysts. An ovarian cyst is a cyst, which is a solid or fluid-filled sac/pocket, on or within the surface of an ovary. For a further diagnosis, ask your doctor for a pelvic exam or a transvaginal ultrasound."
    )
  else:
    print(
      "Yay! Your symptoms show that you are not at risk for ovarian cysts.")


# check pcos
def check_pcos():
  s = 0
  for sym in sympcos:
    s += symptoms[sym]
  if len(sympcos) / 2 <= s:
    print(
      "\nYou may be at risk for Polycystic Ovary Syndrome (PCOS). PCOS is a hormonal disorder that leads to the ovaries becoming enlarged and small cysts forming on the outer edges. For a further diagnosis, ask your doctor for a pelvic exam, blood tests, and an ultrasound."
    )
  else:
    print(
      "Yay! Your symptoms show that you are not at risk for Polycystic Ovary Syndrome (PCOS)."
    )


#check endometriosis
def check_endometriosis():
  s = 0
  for sym in symendometriosis:
    s += symptoms[sym]
  if len(symendometriosis) / 2 <= s:
    print(
      "\nYou may be at risk for endometriosis. This is when the uterine lining that sheds every month is growing on the outside of the uterus. For a further diagnosis, ask your doctor for a CA125 test."
    )
  else:
    print(
      "Yay! Your symptoms show that you are not at risk for endomeitriosis.")


#check polyps
def check_polyps():
  s = 0
  for sym in sympolyops:
    s += symptoms[sym]
  if len(sympolyops) / 2 <= s:
    print(
      "\nYou may be at risk for polyps. Polyps are fingerlike tissue growths on the cervix. For a further diagnosis, we recommend you get a pelvic exam and a pap smear."
    )
  else:
    print("Yay! Your symptoms show that you are not at risk for polyops.")

def run_everything():
  introduction()
  ask_age()
  ask_height()
  ask_first_period()
  ask_medications()
  ask_symptoms()
  print("\n" * 4)
  check_menopause()
  check_first_period_irregularities()
  check_medications()
  check_ovarian_cyst()
  check_pcos()
  check_endometriosis()
  check_polyps()
  print("\n" * 3)
 
run_everything()
