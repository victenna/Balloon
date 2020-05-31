import turtle,time,random
wn=turtle.Screen()
turtle.tracer(3)
wn.setup(1200,800)
wn.bgcolor('light blue')
wn.bgpic('background2.gif')

clr=['red','blue','yellow','lime','gold']
clr1=['shredred.gif','shredblue.gif','shredyellow.gif','shredlime.gif','shredgold.gif']

for i in range(5):
    wn.addshape(clr1[i])
    
wn.addshape('boy00.gif')
wn.addshape('boy01.gif')
wn.addshape('boy12.gif')
wn.addshape('girl2.gif')
wn.addshape('girl3.gif')

wn.addshape('rope1.gif')
    

boy=turtle.Turtle()
boy.up()
boy.hideturtle()
boy.shape('boy00.gif')
boy.goto(-40,-200)


boy1=turtle.Turtle()
boy1.shape('boy12.gif')
boy1.up()
boy1.hideturtle()
boy1.goto(-400,-200)

boy2=turtle.Turtle()
boy2.shape('boy12.gif')
boy2.up()
boy2.hideturtle()
boy2.goto(-400,-200)


girl=turtle.Turtle()
girl.shape('girl2.gif')
girl.up()
girl.hideturtle()
girl.goto(420,-140)
girl.showturtle()



balloon=turtle.Turtle('circle')
balloon.hideturtle()
balloon.shapesize(2.2,3)
balloon.color(clr[0])
balloon.setheading(90)
balloon.up()
balloon.goto(-11,-120)

balloon1=balloon.clone()
balloon1.hideturtle()
balloon1.goto(-450,-150)
balloon1.color(clr[1])
balloon1.showturtle()

balloon2=balloon.clone()
balloon2.goto(-340,-150)
balloon2.color(clr[2])
balloon2.showturtle()

balloon3=balloon.clone()
balloon3.goto(450,-80)
balloon3.color(clr[2])
balloon3.showturtle()


cord=turtle.Turtle()
cord.up()
cord.hideturtle()
cord.goto(-10,-155)#!!!!!!!!!!!!!
cord.shape('rope1.gif')

cord1=cord.clone()
cord1.up()
cord1.hideturtle()
cord1.goto(450,-125)#!!!!!!!!!!!!!
#cord1.showturtle()
cord2=cord.clone()
cord2.up()
cord2.hideturtle()
cord2.goto(-450,-150)

cord3=cord.clone()
cord3.up()
cord3.hideturtle()
cord3.goto(-330,-150)



boy.showturtle()
balloon.showturtle()
cord.showturtle()
boy1.showturtle()

shred=turtle.Turtle()
shred.up()
shred.hideturtle()
shred.goto(-40,200)

shred1=shred.clone()
shred1.up()
shred1.hideturtle()
shred1.goto(-450,200)

shred2=shred.clone()
shred2.up()
shred2.hideturtle()
shred2.goto(-340,200)

shred3=shred.clone()
shred3.up()
shred3.hideturtle()
shred3.goto(450,200)


q=-1
turtle.tracer(3)


    
while True:
    girl.shape('girl2.gif')
    balloon.shapesize(2.2,3)
    balloon.hideturtle()
    balloon.goto(-11,-120)
    balloon.showturtle()
    
    balloon1.shapesize(2.2,3)
    balloon1.hideturtle()
    balloon1.goto(-450,-150)
    balloon1.showturtle()
    
    balloon2.shapesize(2.2,3)
    balloon2.hideturtle()
    balloon2.goto(-340,-150)
    balloon2.showturtle()
    
    balloon3.shapesize(2.2,3)
    balloon3.hideturtle()
    balloon3.goto(450,-80)
    balloon3.showturtle()
    q=q+1
    q11=q%5
    
    q2=q+2
    q21=q2%5
    
    q3=q+3
    q31=q3%5
    
    q4=q+4
    q41=q4%5
    
    
    
    balloon.color(clr[q11])
    balloon1.color(clr[q21])
    balloon2.color(clr[q31])
    balloon3.color(clr[q41])
    shred.hideturtle()
    shred1.hideturtle()
    shred2.hideturtle()
    shred3.hideturtle()
    
    cord.hideturtle()
    cord.goto(-10,-160)
    cord.showturtle()
    
    cord1.hideturtle()
    cord1.goto(450,-125)
    cord1.showturtle()
    for i in range(25):
        #girl.shape('girl2.gif')
        X=balloon.xcor()
        Y=balloon.ycor()
        
        X3=balloon3.xcor()
        Y3=balloon3.ycor()
        
        cord.setposition(X,Y-20-2.5*i)
        cord1.setposition(X3,Y3-20-4*i)
        cord2.showturtle()
        cord3.showturtle()
        cord2.setposition(-450,Y3-90-0.8*i)
        cord3.setposition(-330,Y3-90-0.8*i)
        
        balloon.fd(14)
        balloon1.fd(10)
        balloon2.fd(11)
        balloon3.fd(8)
        
        balloon.shapesize(2.2*(1+0.06*i),3*(1+0.06*i))
        balloon1.shapesize(2.2*(1+0.06*i),3*(1+0.06*i))
        balloon2.shapesize(2.2*(1+0.06*i),3*(1+0.06*i))
        balloon3.shapesize(2.2*(1+0.06*i),3*(1+0.06*i))
        time.sleep(0.05)
        if i==0:
            boy.shape('boy00.gif')
            boy1.shape('boy12.gif')
            girl.shape('girl2.gif')
            
            
            time.sleep(0.2)
        if i==1:
            boy.shape('boy01.gif')
            boy1.shape('boy12.gif')
        if i==10:
            girl.shape('girl3.gif')
                
        if i==23:
            balloon.shapesize(0.01)
            balloon1.shapesize(0.01)
            cord.hideturtle()
            cord1.hideturtle()
            balloon.hideturtle()
            balloon1.hideturtle()
            balloon2.hideturtle()
            balloon3.hideturtle()
            cord2.hideturtle()
            cord3.hideturtle()
            shred.showturtle() 
            shred.shape(clr1[q11])
            
            shred1.showturtle() 
            shred1.shape(clr1[q21])
            
            shred2.showturtle() 
            shred2.shape(clr1[q31])
            
            shred3.showturtle() 
            shred3.shape(clr1[q41])
            boy.shape('boy00.gif')
            girl.shape('girl2.gif')
            time.sleep(0.5)
