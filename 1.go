package main
import "fmt"

func main(){	
	var n,a,x int
	var data [100]int
	var min1,min2 int
	var max1,max2 int
	
	fmt.Scanln(&n,&a)
	
	for i:=0; i < n; i++{
		fmt.Scan(&x)
		data[i] = x
	}
	
	min1,min2 = min(data,n)
	max1,max2 = max(data,n)
	
	if ganjilGenap(a) == "genap"{
		fmt.Println(min2,min1)
	}else{
		fmt.Println(max1,max2)
	}
}

func ganjilGenap(a int)string{
	if a%2 == 0{
		return "genap"
	}else{
		return "ganjil"
	}
}

func min(data [100]int,n int)(int,int){
	min1 := data[0]
	min2 := data[0]
	
	for i:=0; i < n; i++{
		if min1 > data[i]{
			min1 = data[i]
		}
	}
		
	for i:=0; i < n && data[i] != min1; i++{
		if min2 > data[i]{
			min2 = data[i]
		}
	}
	return min1,min2
}

func max(data [100]int,n int)(int,int){
	max1 := data[0]
	max2 := data[0]
	
	for i:=0; i < n; i++{
		if max1 < data[i]{
			max1 = data[i]
		}
	}
		
	for i:=0; i < n && data[i] != max1; i++{
		if max2 < data[i]{
			max2 = data[i]
		}
	}
	return max1,max2
}
		