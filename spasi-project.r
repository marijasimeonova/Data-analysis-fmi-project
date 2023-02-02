grades <- read.csv("results-2019.csv")
attach(grades)

bel_totals <- grades$БЕЛ.Брой #Number of students that took the BEL exam
bel_averages <- sub(",", ".", (grades$БЕЛ.Ср.успех)) #The average of the BEL Exam
bel_averages <- as.double(bel_averages)

bel_averages
bel_total_averages <- bel_totals * bel_averages
bel_total_averages

bel_no_of_students <- sum(grades$БЕЛ.Брой)
bel_total <- sum(bel_total_averages)

bel_average <- bel_total / bel_no_of_students
bel_average

#---------math------------------
math_totals <- grades$МАТ.Брой #No. that took the Math exam
math_averages <- sub(",", ".", (grades$МАТ.Ср.успех)) #average of the math exam
math_averages <- as.double(math_averages)

math_total_averages <- math_totals * math_averages
math_no_of_students <- sum(grades$МАТ.Брой)
math_total <- sum(math_total_averages)
math_average <- math_total / math_no_of_students
math_average

#---------------------------2021-----------------------------------------
grades_2021 <- read.csv("results-2021.csv")
attach(grades_2021)

bel_totals_2021 <- grades_2021$БЕЛ.Брой #Number of students that took the BEL exam
bel_averages_2021 <- sub(",", ".", (grades_2021$БЕЛ.Ср.успех)) #The average of the BEL Exam
bel_averages_2021 <- as.double(bel_averages_2021)

bel_total_averages_2021 <- bel_totals_2021 * bel_averages_2021
bel_total_averages_2021

bel_no_of_students_2021 <- sum(grades_2021$БЕЛ.Брой)
bel_total_2021 <- sum(bel_total_averages_2021)

bel_average_2021 <- bel_total_2021 / bel_no_of_students_2021
bel_average_2021

#---------math------------------
math_totals_2021 <- grades_2021$МАТ.Брой #No. that took the Math exam
math_averages_2021 <- sub(",", ".", (grades_2021$МАТ.Ср.успех)) #average of the math exam
math_averages_2021 <- as.double(math_averages_2021)

math_total_averages_2021 <- math_totals_2021 * math_averages_2021
math_no_of_students_2021 <- sum(grades_2021$МАТ.Брой)
math_total_2021 <- sum(math_total_averages_2021)
math_average_2021 <- math_total_2021 / math_no_of_students_2021
math_average_2021

