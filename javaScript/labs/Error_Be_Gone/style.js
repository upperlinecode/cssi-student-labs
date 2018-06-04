function uglyCode(arr, num){
if(arr.length == 0) return "array length is zero"
else{

if(arr.length > 5) for(var i = 0; i < arr.length; i++) arr[i]=num
}

return arr

}

var array=[0,0,0,0,0,0]
console.log(
  uglyCode(array,5))
