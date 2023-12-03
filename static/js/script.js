
function validation() {

  if (checkname() == false || checkaddress() == false || checkage()==false || checkgender()==false || checkpass()==false || checknum()==false || checkblood()==false)  {

    return false;
  }
  // if (checkname()==false){
  //   return false;
  // }
  // if (checkaddress()==false){
  //   return false;
  // }
  return true;

}
function checkaddress(){
  var address = document.getElementById("address").value;
  var add = document.getElementById("address");
  
  if (address == "" || address.length < 3) {
    document.getElementById("adderror").innerHTML=
    "address must be mentioned";
    add.style.border = "3px solid red";
    return false;
  }
  else {
    return true;
  }
}
function checkname() {
  var name = document.getElementById("fname").value;
  var x = document.getElementById("fname");
  
  if (name == "" || name.length < 3) {
    document.getElementById("nameer").innerHTML=
    "name must be mentioned";
    x.style.border = "3px solid red";
    return false;
  }
  else {
    return true;
  }

  
}
function checkage(){
  var age = document.getElementById("age").value;
  var a = document.getElementById("age");
  
  if (age == "" ) {
    document.getElementById("ageerror").innerHTML=
    "age must be mentioned";
    a.style.border = "3px solid red";
    return false;
  }
  else {
    return true;
  }

}

function checkgender(){
  if(document.getElementById("gender").checked==false)
  {
    document.getElementById("gendererror").innerHTML=
    "gender must be specified";
    return false;
  }
  return true; 

}

function checkpass(){
  var password = document.getElementById("password").value;
  var x = document.getElementById("password");
  
  if (password == "" || password.length < 3) {
    document.getElementById("passerror").innerHTML=
    "password must be mentioned";
    x.style.border = "3px solid red";
    return false;
  }
  else {
    return true;
}
}

function checknum(){
  var num = document.getElementById("number").value;
  var x = document.getElementById("number");
  
  if (num == "" || num.length < 3) {
    document.getElementById("numerror").innerHTML=
    "number must be mentioned";
    x.style.border = "3px solid red";
    return false;
  }
  else {
    return true;
}
}

function checkblood(){
  var bl = document.getElementById("blood_group").value;
  if (bl=="blood"){
    document.getElementById("blooderror").innerHTML="enter your blood group";
    return false;
  }
  else{
    true;
  }
}