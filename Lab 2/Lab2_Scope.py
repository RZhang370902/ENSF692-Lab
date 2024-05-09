# ENSF 592 Spring 2023
# May 9 Lab 2
# Exercise 2


# Trace through the execution of the following program. 
# Answer the questions in the comments with your group members.
# After discussing, use print statements to confirm your answers.

foo = 100
bar = foo
foo + bar

print("Point 1")
print("value of foo is", foo)
print("type of foo is", type(foo))
print("value of bar is", bar)
print("type of bar is", type(foo))
print('\n' * 2)

# POINT 1
# What is the value of foo at this point? 100 correct
# What is the type of foo at this point? int correct
# What is the value of bar at this point? 100 correct
# What is the type of bar at this point? int correct

spam = foo + bar #foo = 100, bar = 100, so spam = 200
foo += 50 #foo = 150
eggs = foo + bar #foo = 150, bar = 100, so eggs = 250
ham = [1, 2, 3]
baz = ham
ham.append(bar)

print("Point 2")
print("value of foo is", foo)
print("value of bar is", bar)
print("value of spam is", spam)
print("value of spam is", eggs)
print("value of ham is", ham)
print("value of baz is", baz)
print('\n' * 2)

# POINT 2
# What is the value of foo at this point? foo = 150 correct
# What is the value of bar at this point? bar = 100 correct
# What is the value of spam at this point? spam = 200 correct
# What is the value of eggs at this point? eggs = 250 correct
# What is the value of ham at this point? ham = [1, 2, 3, 100]
# What is the value of baz at this point? baz = [1, 2, 3, 100] object got updated, there is no assignment to baz

eggs = "Python is very flexible!"
spam = ham # ham = [1, 2, 3, 100] so spam = [1, 2, 3, 100], also points spam to baz
ham = bar # bar = 100, so ham = 100
bar += bar # bar = 100, so bar now = 200
foo = eggs #eggs = "Python is very flexible!" so foo = "Python is very flexible"
eggs = bar + ham # bar = 200, ham =100, so eggs = 300
baz.append(bar) #baz = [1, 2, 3, 100], bar = 200, so baz now is [1, 2, 3, 100, 200] also affect line 31

print("Point 3")
print("value of foo is", foo)
print("value of bar is", bar)
print("value of spam is", spam)
print("value of eggs is", eggs)
print("value of ham is", ham)
print("value of baz is", baz)
print('\n' * 2)



# POINT 3
# What is the value of foo at this point? foo = "Python is very flexible"
# What is the value of bar at this point? bar = 200
# What is the value of spam at this point? spam = [1, 2, 3, 100] incorrect spam = ham, pointing to same object, baz also points to the same obeject
# What is the value of eggs at this point? eggs = 300
# What is the value of ham at this point? ham = 100
# What is the value of baz at this point? baz = [1, 2, 3, 100, 200]

# Print out the types and final values of each variable.
