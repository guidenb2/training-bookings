import sys

def maximum(tuesday, thursday, saturday, sunday):
   len_tues = len(tuesday)
   len_thur = len(thursday)
   len_sat = len(saturday)
   len_sun = len(sunday)
   lst = [len_tues, len_thur, len_sat, len_sun]
   return max(lst)

def sort_into_days(groups):
   seven = []
   seven_thirty = []
   eight = []
   eight_thirty = []
   for group in groups:
      tokens = group.strip().split("\n")
      if tokens[0] == "7:00":
         tokens = tokens[1:]
         for x in tokens:
            if x != "":
               seven.append(x)
         seven.append("FLAG")
      if tokens[0] == "7:30":
         tokens = tokens[1:]
         for x in tokens:
            if x != "":
               seven_thirty.append(x)
         seven_thirty.append("FLAG")
      if tokens[0] == "8:00":
         tokens = tokens[1:]
         for x in tokens:
            if x != "":
               eight.append(x)
         eight.append("FLAG")
      if tokens[0] == "8:30":
         tokens = tokens[1:]
         for x in tokens:
            if x != "":
               eight_thirty.append(x)
         eight_thirty.append("FLAG")
   return seven, seven_thirty, eight, eight_thirty

def boxify(lst):
   s = []
   for line in lst:
      if line == "BOOKER:":
         s.append("+--------------------------------------+")
         s.append("| {:<36} |".format(line))
      elif line == "POD 1:":
         s.append("| {:<36} |".format(line))
         s.append("|--------- {:<27} |".format(""))
      elif line == "POD 2:":
         s.append("| {:<36} |".format(line))
         s.append("|--------- {:<27} |".format(""))
      elif line == "FLAG":
         s.append("+--------------------------------------+")
         s.append("  {:<36}  ".format(""))
      else:
         s.append("| {:<36} |".format(line))
   return s

def printer(time1, time2, time3, time4):
   print("| {:^37} | {:^38} | {:^38} | {:^37} |".format("7:00", "7:30", "8:00", "8:30"))
   print("|{}|\n|{:161}|".format("-" * 161, ""))
   most = maximum(time1, time2, time3, time4)
   line = 0
   flag = 0
   while line < most:
      try:
         print(time1[line], end =" ") 
      except:
         print("  {:<36}  ".format(""), end =" ")
      try:
         print(time2[line], end =" ") 
      except:
         print("  {:<36}  ".format(""), end =" ")
      try:
         print(time3[line], end =" ") 
      except:
         print("  {:<36}  ".format(""), end =" ")
      try:
         print(time4[line], end =" ") 
      except:
         print("  {:<36}  ".format(""), end =" ")
      print("")
      line += 1
   

def main():
   file = sys.argv[1]
   with open(file) as fd:
      filelines = fd.read()
      lst = filelines.strip().split("#")
      lst = lst[:-1]
   time1, time2, time3, time4 = sort_into_days(lst)
   time1 = boxify(time1)
   time2 = boxify(time2)
   time3 = boxify(time3)
   time4 = boxify(time4)
   printer(time1, time2, time3, time4)

if __name__ == "__main__":
   main()