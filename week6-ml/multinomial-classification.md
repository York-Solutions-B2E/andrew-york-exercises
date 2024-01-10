Strategies for multinomial classification (3 or more classes)

Any inherently binary classifier will likely do 1-vs-1 or 1-vs-Rest behind the scenes, 
splitting multi-class classification problems into several binary classification problems

e.g. classes are RGB

1-vs-1
SVM could do RvB, RvG and BvG

1-vs-Rest
RvB&G, BvR&G, GvR&B