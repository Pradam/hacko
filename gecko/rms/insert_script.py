from random import randint
from .models import HistoryData
men = ['Aarav', 'Vivaan', 'Aditya', 'Vihaan', 'Arjun', 'Reyansh', 'Muhammad', 'Sai', 'Arnav', 'Ayaan', 'Aryan', 'Ansh', 'Shaurya', 'Madhavaditya', 'Dhruv', 'Krishna', 'Krish', 'Atharv', 'Ishaan', 'Raahithya', 'Kabir', 'Arush', 'Rudra', 'Anik', 'Om', 'Ajay', 'Akshay', 'Chetan', 'Manish', 'Manoj', 'Mohan', 'Prem', 'Rahul', 'Rajesh', 'Ramesh', 'Sanjay', 'Rohit', 'Vijay', 'Vinod', 'Abhay', 'Bodhi', 'Rajiv', 'Kamal', 'Navin', 'Rohan', 'Advik', 'Ayush', 'Siddharth', 'Advaith', 'Raghav', 'Dev', 'Parth', 'Abdul', 'Shivansh', 'Samar', 'Pratyush', 'Neil', 'Devansh', 'Yash', 'Tejas', 'Zayn', 'Darsh', 'Sarthak', 'Gautam', 'Agastya', 'Samarth', 'Pranav', 'Daksh', 'Aadesh', 'Aakash', 'Abhimanyu', 'Adit', 'Adnan', 'Amandeep', 'Bharat', 'Chandan', 'Dalip', 'Deepak', 'Dinesh', 'Eklavya', 'Gaurav', 'Govinda', 'Gurdeep', 'Hari', 'Harish', 'Harsh', 'Hemant', 'Sabhya', 'Jai', 'Rishabh', 'Hrithik', 'Indra', 'Shakti', 'Jagan', 'Karan', 'Karthik', 'Kushal', 'Lalit', 'Mehul', 'Nakul',]
women = ['Saanvi', 'Aadya', 'Kiara', 'Diya', 'Pihu', 'Prisha', 'Ananya', 'Fatima', 'Myra', 'Sarah', 'Aarohi', 'Aaradhya', 'Aarya', 'Sri', 'Pari', 'Anvi', 'Riya', 'Siya', 'Kavya', 'Ayesha', 'Anika', 'Anaya', 'Advika', 'Aditi', 'Maryam', 'Riddhi', 'Meera', 'Aanya', 'Ahana', 'Aayra', 'Sai', 'Maria', 'Samaira', 'Swara', 'Princess', 'Navya', 'Jia', 'Isha', 'Avani', 'Sophia', 'Kyra', 'Shreya', 'Ira', 'Aadriti', 'Amyra', 'Yazhini', 'Vanya', 'Nisha', 'Mishka', 'Nitara', 'Angel', 'Mary', 'Mahira', 'Aarushi', 'Sanaya', 'Maithreyi', 'Manya', 'Drishya', 'Kashvi', 'Inaaya', 'Ishika', 'Aavya', 'Aadhira', 'Anshika', 'Misha', 'Mia', 'Michelle', 'Ishani', 'Veda', 'Tania', 'Shanaya', 'Reeva', 'Trisha', 'Hayaa', 'Vedanshi', 'Tia', 'Sahana', 'Vrinda', 'Sana', 'Shivanya', 'Pranavi', 'Naira', 'Manasvi', 'Aradhana', 'Mishti', 'Nitya', 'Dhvani', 'Ayat', 'Elizabeth', 'Divija', 'Eleanor', 'Gabriella', 'Emma', 'Zoe', 'Maahi', 'Aarna', 'Disha', 'Vaishnavi', 'Saira', 'Zara']
def get_int(start, end):
   while True:
       yield(randint(start, end))
gi_100 = get_int(0, 99).__next__
gi_3 = get_int(1,3).__next__
alcohol = get_int(1,3).__next__
gi_2 = get_int(1,2).__next__
adhar = get_int(1,10**13-1).__next__
claimed = get_int(1,3).__next__
smoke = get_int(1,3).__next__
age = get_int(18,70).__next__
mbr = get_int(1,3).__next__
for i in range(1000):
  gender = gi_2()
  father = men[gi_100()]
  name = {1: men, 2:women}[gender][gi_100()]
  name = '%s %s' % (name, father)
  kwargs = dict(gender=gender, name=name, is_alcoholic=alcohol(),
                aadhar_id=adhar(), is_smoker=smoke(),claimed=claimed(),age=age(),is_member=mbr())
  print (kwargs)
  HistoryData.objects.create(**kwargs)
  
