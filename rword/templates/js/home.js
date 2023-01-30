//웹 방문 시 로그인 Modal 자동 시작
$(window).on('load',function(){
    //배경클릭하여 빠져나오기 불가하도록 제작
    $('#ModalForm').data('bs.modal',null); 
    $('#ModalForm').modal({backdrop:'static',keyboard:false})
    $('#ModalForm').modal('show'); 
});

const loginbtn = document.querySelector('.loginbtn');
const signupbtn = document.querySelector('.signupbtn');
const alertb1 = document.querySelector('.alertb1');
const alertb2 = document.querySelector('.alertb2');
const btnclose = document.querySelector('.btn-close');
const gotoSignUp = document.querySelector('.gsignup');
const randommenu = document.querySelector('.randommenu');
var idlogin;
var passwordlogin;
var idsignup;
var passwordsignup;

//효과이므로 넣어야 합니다!
$(document).ready(
    //randommenu(nav바 '랜덤단어 생성하기')를 누르면 홈페이지에서 해당 부분으로 스르륵 자동으로 이동해야 함
    function(){		
        $('.randommenu').click(function()
        {			
            var offset = $('#level').offset();
            //animate()메서드를 이용해서 선택한 태그의 스크롤 위치를 지정해서 0.4초 동안 부드럽게 해당 위치로 이동함 
            $('html').animate({scrollTop : offset.top}, 400);		
        });	

        $(window).scroll( function(){
			//해당 위치까지 스크롤하면 내용이 스르륵 나타나도록 함
            $('.ignovelcontent').each( function(i){
                
                var bottom_of_element = $(this).offset().top + $(this).outerHeight() / 3;
                var bottom_of_window = $(window).scrollTop() + $(window).height();
                
                if( bottom_of_window > bottom_of_element ){
                    $(this).animate({'opacity':'1'},700);
                }
            }); 
        });
    }
);

//백엔드 팀원분들께서 구현해주신 부분
//로그인 버튼을 눌렀을 때
loginbtn.addEventListener("click",function(){

    idlogin = document.getElementById('Username1').value;
    passwordlogin = document.getElementById('Password1').value;
    //아무것도 적지 않았는데 버튼을 눌렀다면 경고문.
    if(!idlogin || !passwordlogin){
        alert('아이디 혹은 비밀번호를 입력하세요.')
    }
    else{ //적고 눌렀다면 비밀번호 맞나 확인
        //아닐 경우
        alert('아이다 또는 비밀번호를 잘못 입력하였습니다.')
        //맞을 경우 모달창 닫기
        $('#ModalForm').modal('hide');
    }
})


//본격적인 랜덤 페이지//
const main = document.querySelector("#main");
const level = document.querySelector("#level");
const random = document.querySelector("#random");
const sentence = document.querySelector("#sentence");

//랜덤 단어 잘 나오나 실험
const wordlist = ["i","love","you","hamburger","cat","hate"]; //시험용 리스트

//랜덤단어를 클릭했을때 단어가 나타나도록 한다.백엔드 팀원분들께서 구현해주신 부분입니다!
document.querySelectorAll(".btngroup")[0].addEventListener("click",function(e){
    console.log("클릭함")
    tabBtn(e.target.dataset.id);
});

var currentw;
//랜덤단어를 클릭했을때 단어가 나타나는데 효과를 넣어 나타나도록 한다.
function tabBtn(a){
    document.querySelectorAll(".btncheck")[a].addEventListener("click",function(){
        for(let i =0;i<document.querySelectorAll(".btncheck").length;i++){
            //document.querySelectorAll(".lwords")[i].style.display = "none";
            console.log("도는중");
            document.querySelectorAll(".lwords")[i].style.display = 'none';
        }
        document.querySelectorAll(".lwords")[a].classList.add("focus-in-expand");
        document.querySelectorAll(".lwords")[a].style.display='block';
        //글자를 받아와서 세팅해주어야 함.
        currentw = []
        var clickedwords =  document.querySelectorAll(".lwords")[a];
        for(let i =0;i<clickedwords.querySelectorAll('.wordspan').length;i++){
            clickedwords.querySelectorAll('.wordspan')[i].innerHTML=makingWords();
        }
    })
}

//랜덤단어를 클릭했을때 단어가 나타나도록 한다.백엔드 팀원분들께서 구현해주신 부분입니다!
function makingWords()
{
    var n = wordlist.length;
    //말한 만큼의 단어를 가져와서 뱉기
    let num = Math.floor(Math.random() * n);
    currentw.push(wordlist[num]);
    return wordlist[num];
}

//제출버튼을 누를 때 포함하는 단어가 다 있는지 확인하고 보내야 함.
const submitbtn = document.querySelector('.submitbtn');
var oneSentence;

submitbtn.addEventListener("click",function(){
    //포함하는 단어 다 있나 확인
    console.log(currentw)
    //1. 값을 받아오고(=유저가 쓴 문장)
    oneSentence= document.querySelector('.onesentence').value;
    //2. 있나 확인
    let flag = true;
    for(let i=0;i<currentw.length;i++)
    {
        if(oneSentence.indexOf(currentw[i]) < 0 ) 
        {
            flag= false;
            console.log(oneSentence.indexOf(currentw[i]));
            break;
        }
    }

    if(flag) //3. 있으면
    {
        alert('다 넣음.');
        //문장게시판으로 이동합니다.
    }
    else{
        alert('제시된 랜덤단어를 모두 넣지 않으셨습니다.');
        
    }
})


//메뉴 호버시 다른 것들은 꺼지고 그것만 살아남게.

/*document.querySelectorAll(".menugroup")[0].addEventListener("mouseover",function(e){
    tabBtn2(e.target.dataset.mid);
});

function tabBtn2(a){
    document.querySelectorAll(".menu")[a].addEventListener("mouseover",function(){
        for(let i =0;i<document.querySelectorAll(".menu").length;i++){
            document.querySelectorAll(".menu")[i].style.color = 'black';
        }
        document.querySelectorAll(".menu")[a].style.color='white';
    })
}

document.querySelectorAll(".menugroup")[0].addEventListener("mouseout",function(e){
    for(let i =0;i<document.querySelectorAll(".menu").length;i++){
        document.querySelectorAll(".menu")[i].style.color = 'white';
    }
});
*/

//내용을 슬라이드
/*const ignovelcontent = document.querySelector(".ignovelcontent");

const yap = document.querySelector(".yap");
yap.addEventListener("click",function(){
    setTimeout(()=>{
        ignovelcontent.style.WebkitAnimation = "fadeIn 1s";
        ignovelcontent.style.animation = "fadeIn 1s";
        setTimeout(() => {
            ignovelcontent.style.display = "block";            
        }, 450);
    },450);
})
*/

document.querySelectorAll('.go_btn').forEach(
    button => button.innerHTML = '<div><span>' + button.textContent.trim().split('').join('</span><span>') + '</span></div>');
