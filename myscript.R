# my test R script



sum_xy=function(x,y)
{

  tot=x+y
  return(tot) 

}



x=c(1,2,3,4)
y=c(1,2,3,4)

result <- sum_xy(x,y)
write.table(result,"results.txt")

