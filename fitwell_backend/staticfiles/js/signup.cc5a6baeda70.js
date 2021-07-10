window.onload = (e) => {
  let current_fs, next_fs; //fieldsets
  button1 = document.getElementById('next1');

  button1.onclick = (e) => {
        if (formValidation1()){
    current_fs = button1.parentElement.parentElement;
    next_fs = button1.parentElement.parentElement.nextElementSibling;
    current_fs.style.display = 'none';
    next_fs.style.display = 'block';
    document.getElementById('img').style.backgroundImage =
      'url(/static/images/sign-up-bg2.png)';
    step1 = document.getElementById('step1').classList.add('active');

}else{
//    alert("Please provide the required information before proceeding");
};

  };

  button2 = document.getElementById('next2');
  button2.onclick = (e) => {
  if (formValidation2()){
    current_fs = button2.parentElement.parentElement;
    next_fs = button2.parentElement.parentElement.nextElementSibling;
    current_fs.style.display = 'none';
    next_fs.style.display = 'block';
    console.log(document.getElementById('img').style.background);
    step1 = document.getElementById('step2').classList.add('active');
    document.getElementById('img').style.backgroundImage =
      'url(/static/images/sign-up-bg3.png)';
   }else{
//    alert("Please provide the required information before proceeding");
  };
};
};

function formValidation1(){
    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var email = document.getElementById('email').value;
    var dob  = document.getElementById('date').value;
    var message = true;

    if (fname == ""){
//        alert("First Name field is mandatory. ")
//        document.getElementById('fname').focus();
        document.getElementById('fname_error').innerHTML = "First Name Field is Required";
        message = false;
//        return false;
        }else{
          if (document.getElementById('fname').value.length > 0){
            document.getElementById('fname_error').innerHTML = "";
            }
        }

    if (lname == ""){
//        alert("Last Name field is Required. ")
//        document.getElementById('lname').focus();
        document.getElementById('lname_error').innerHTML = "Last Name Field is Required";
        message = false;
//        return false;
        }else{
             if (document.getElementById('lname').value.length > 0){
                document.getElementById('lname_error').innerHTML = "";
            }
        }

    if (email == ""){
//        alert("email field is Required. ")
//        document.getElementById('email').focus();
        document.getElementById('email_error').innerHTML = "email Field is Required";
        message = false;
//        return false;
        }else{
            if (email.includes("@") && (email.includes("."))){

                  if (document.getElementById('email').value.length > 0){
                    document.getElementById('email_error').innerHTML = "";
                }
            }else{
//            alert("email is invalid. ")
//            document.getElementById('email').focus();
            document.getElementById('email_error').innerHTML = "email  is invalid";
            message = false;
//                return false;
            }
        }
    if (dob == ""){
//        alert("Date of birth field is Required. ")
//        document.getElementById('date').focus();
        document.getElementById('dob_error').innerHTML = "Date of Birth Field is Required";
        message = false;
//        return false;
        }else{
             if (document.getElementById('date').value.length  > 0 ){
        document.getElementById('dob_error').innerHTML = "";
    }

        }

return message;
}

function formValidation2(){
    var weight = document.getElementById('weight').value;
    var height = document.getElementById('height').value;

    var message = true;

    if (weight == ""){
//        alert("First Name field is mandatory. ")
//        document.getElementById('weight').focus();
        document.getElementById('weight_error').innerHTML = "Weight Field is Required";
        message = false;
//        return false;
        }else{

      if (document.getElementById('weight').value.length > 0 ){
        document.getElementById('weight_error').innerHTML = "";
    }
        }

    if (height == ""){
//        alert("Last Name field is Required. ")
//        document.getElementById('height').focus();
        document.getElementById('height_error').innerHTML = "Height Field is Required";
        message = false;
//        return false;
        }else{

       if (document.getElementById('height').value.length > 0 ){
        document.getElementById('height_error').innerHTML = "";
    }

        }

return message;
}

function formValidation3(){
    var pass1 = document.getElementById('pword1').value;
    var pass2 = document.getElementById('pword2').value;
    var security_question = document.getElementById('squestion').value;
    var security_answer = document.getElementById('squestionanswer').value;

    var pass1_check = false
    var pass2_check = false
    var sq_check = false
    var sqa_check = false

    var message = true;

    if (pass1 == "" && pass2 == ""){
//        alert("First Name field is mandatory. ")
//        document.getElementById('pword1').focus();
        document.getElementById('pword1_error').innerHTML = "password is Required";
        message = false;
//        return false;
        }else{
            if (pass1.length < 8 || pass2.length < 8){
//            document.getElementById('pword1').focus();
            document.getElementById('pword1_error').innerHTML = "password should not be less than 8 character";
            message = false;
            }else{
                if (pass1 != pass2){
//                    document.getElementById('pword1').focus();
                    document.getElementById('pword1_error').innerHTML = "password do not match";
                    message = false;
                }else{
                        if (document.getElementById('pword1').value.length > 0 ){
                        document.getElementById('pword1_error').innerHTML = "";
                        pass1_check = true;
                        }

                      if (document.getElementById('pword2').value.length > 0 ){
                        document.getElementById('pword2_error').innerHTML = "";
                        pass2_check = true;
                    }
                }
            }

        }

    if (security_question == "Enter security question"){
//        alert("Last Name field is Required. ")
//        document.getElementById('squestion').focus();
        document.getElementById('squestion_error').innerHTML = "Security Question is  Field is Required";
        message = false;
//        return false;
        }else{
                if (document.getElementById('squestion').value.length > 0 ){
                document.getElementById('squestion_error').innerHTML = "";
                sq_check = true
                }
        }

       if (security_answer == ""){
//        alert("Last Name field is Required. ")
//            document.getElementById('squestionanswer').focus();
            document.getElementById('squestionanswer_error').innerHTML = "Security Answer Field is Required";
            message = false;
        //        return false;
    } else {

      if (document.getElementById('squestionanswer').value.length > 0 ){
        document.getElementById('squestionanswer_error').innerHTML = "";
        sqa_check = true

    }
    }

 if (pass1_check == true && pass2_check == true && sqa_check == true && sqa_check == true){
    return true

}else{
    return false
}

}







