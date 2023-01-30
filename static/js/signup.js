const signupbtn = document.querySelector('.signupbtn');
var myid;
var mypwd;

signupbtn.addEventListener("click", function(){

    myid = document.querySelector('.myid').value;
    mypwd = document.querySelector('.mypwd').value;

    //아무것도 적지 않았는데 버튼을 눌렀다면 
    if(!myid || !mypwd){
        //경고창이 뜨도록
        //Swal.fire('Any fool can use a computer');
        alert("사용자ID와 비밀번호는 필수입력 항목입니다.");


    }
    //뭘적긴 했다면
    else{ 

        console.log("적긴 했습니다.");
        //아이디와 비밀번호가 기존 db와 겹치는지 확인해서
        //안겹친다면 메인 홈페이지로 (home.html로) 이동
       
        




        //겹친다면 경고창 생성
        //alert("사용자ID 또는 비밀번호를 잘못 입력하셨습니다.");
    }

})
    
