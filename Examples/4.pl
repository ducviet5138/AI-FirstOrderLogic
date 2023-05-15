study("Charlie", "CSC135").
study("Olivia", "CSC135").
study("Jack", "CSC131").  
study("Arthur", "CSC134").

teach("Kirke", "CSC135").  
teach("Collins", "CSC131"). 
teach("Collins", "CSC171"). 
teach("Jeniffer", "CSC134").
 
professor(Teacher, Student) :-
    teach(Teacher, Course),
    study(Student, Course).