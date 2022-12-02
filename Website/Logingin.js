function validate()
{
var username=document.getElementById("uname").value;
var password=document.getElementById("psw"). value;
if(username=="Admin" && password=="123")
{   
    window.location.href = "NextWindow.html";
}
else
{
    alert("Login Failed");
}

}