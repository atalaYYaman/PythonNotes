#Assigment3

'''
Coding exercise 1

Using the home_run.csv file, load the DataFrame and print out the number of rows and columns in the Data Frame.
home_run.csv dosyasını kullanarak DataFrame'i yükleyin ve Data Frame'deki satır ve sütun sayısını yazdırın.
'''

#Answer/Cevap
import pandas as pd
import matplotlib
import statistics as sta
#loading our csv

data= pd.read_csv('/home/codio/workspace/csv/home_runs.csv')

# WRITE YOUR CODE HERE
print("Number of rows and columns:", data.shape)

'''
Yukarıda ki kodu yazıp "try it" butonuna bastıktan sonra bende çıkan satır sütun => Row=10 Colums=3
'''

'''
Coding Exercise 2

Using the home_runs.csv file and functions, load the Data Frame and print the first 5 rows of the Data Frame.
home_runs.csv dosyasını ve fonksiyonlarını kullanarak Data Frame yükleyin ve Data Frame ilk 5 satırını yazdırın.

'''

#Answer/Cevap
import pandas as pd
import matplotlib
import statistics as sta
#loading our csv

data= pd.read_csv('/home/codio/workspace/csv/home_runs.csv')

# WRITE YOUR CODE HERE
print(data.head(5))

'''
Çıktı bu Şekilde olacak.

        Player  Home Runs Active Player
0     Barry Bonds        762            No
1      Hank Aaron        755            No
2       Babe Ruth        714            No
3  Alex Rodriguez        696            No
4     Willie Mays        660            No

'''

'''
Coding Exercise 3

Using the home_runs.csv file load the Data Frame and store the following values:
A variable:
home_runs.csv dosyasını kullanarak Veri Çerçevesini yükleyin ve aşağıdaki değerleri kaydedin:

data_mode which stores the mode of our Home Runs column
data_mean which stores the mean of our Home Runs column
data_median which stores the median of our Home Runs column
data_range which stores the range of our Home Runs column
data_sum which stores the sum of our Home Runs column
'''

#Answer/Cevap
import pandas as pd
import matplotlib
import statistics as sta
#loading our csv

data= pd.read_csv('/home/codio/workspace/csv/home_runs.csv')

# WRITE YOUR CODE HERE

data_mode = data['Home Runs'].mode()[0]

data_mean = data['Home Runs'].mean()

data_median = data['Home Runs'].median()

data_range = data['Home Runs'].max() - data['Home Runs'].min()

data_sum = data['Home Runs'].sum()

print(f"Mode: {data_mode}")
print(f"Mean: {data_mean}")
print(f"Median: {data_median}")
print(f"Range: {data_range}")
print(f"Sum: {data_sum}")

'''
Try it dedikten sonra çıkan sonuçları doldurdum.
Bende çıkan sonuçlar:
Mode: 586
Mean: 668.0
Median: 658.0
Range: 176
Sum: 6680
'''

'''
Coding Exercise 4

Using the MOCK_COMPANY_DATA.csv file, load the DataFrame and
print out the name and salary of the employee with the highest salary.

MOCK_COMPANY_DATA.csv dosyasını kullanarak DataFrame'i yükleyin ve en yüksek maaşa sahip çalışanın adını ve
maaşını yazdırın.
'''

#Answer/Cevap
import pandas as pd

data = pd.read_csv('MOCK_COMPANY_DATA.csv')

data['salary'] = data['salary'].replace('[\$,]', '', regex=True).astype(float)

max_salary_employee = data.loc[data['salary'].idxmax()]

employee_name = max_salary_employee['employee_name']
employee_salary = round(max_salary_employee['salary'])  # Round the salary to the nearest integer

print(f"Employee with highest salary: {employee_name}")
print(f"Salary: {employee_salary}")


'''
Coding Exercise 5

Using the MOCK_COMPANY_DATA.csv file, load the DataFrame and print out the average salary for each department.

MOCK_COMPANY_DATA.csv dosyasını kullanarak DataFrame'i yükleyin ve her departman için ortalama maaşı yazdırın.
'''

#Answer/Cevap
import pandas as pd

data = pd.read_csv('MOCK_COMPANY_DATA.csv')

data['salary'] = data['salary'].replace('[\$,]', '', regex=True).astype(float)

average_salaries = data.groupby('department')['salary'].mean()

print(average_salaries)

'''
department
Accounting                  256183.514359
Business Development        263375.998772
Engineering                 295215.528000
Human Resources             307339.032162
Legal                       310626.326053
Marketing                   304885.906154
'''