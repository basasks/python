#################################################################################
# SCRIPT NAME:		/home/basasks/input/py05/input02.sh
# AUTHOR:		BASASKS
# PYTHON VERSION:	Python 3.5.9 
# USAGE:		sh /home/basasks/input/py05/input02.sh	
#################################################################################

<START OF ORIGINAL SCRIPT>

SELECT NAME, EMAIL
FROM NEWDBCOMPANY.EMPLOYEE, NEWDBSCHOOL.STUDENTS, NEWDBCOMPANY.EMPLOYEE_TEMP
WHERE AGE > 20; 

<END OF ORIGINAL SCRIPT>
