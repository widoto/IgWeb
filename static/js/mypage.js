const makenew = document.querySelector('.makenew');

//유저가 쓴 글들의 데이터를 모아와서 

//카드로 마이페이지에 업로드
//현재는 카드가 생성되는 것을 확인하려고 버튼 클릭 이벤트로 설정하였습니다.
makenew.addEventListener("click",function(){
    //새로운게 생겨야.
    var mygallery = document.querySelector(".mygallery");

    var postsh5 = document.createElement('h5');
    postsh5.classList.add('card-title');
    postsh5.innerHTML = "제목입니다"; //유저가 만들었던 한 문장
    var postsp1 = document.createElement('p');
    postsp1.classList.add('card-text');
    postsp1.innerHTML = "안에 들어갈 문장들인데요 어떻게든 길게 써보겠습니다"; //유저가 썼던 설명 내용
    var postsp2 = document.createElement('p');
    postsp2.classList.add('card-text');
    postsp2.classList.add('text-muted');
    postsp2.innerHTML = "- 일반인 게시판 -"
    postsp2.classList.add('carddesigns');

    var postsbody = document.createElement('div');
    postsbody.classList.add('card-body');
    postsbody.classList.add('carddesignb');

    var postscard = document.createElement('div');
    postscard.classList.add('card');

    var posts = document.createElement('div');
    posts.classList.add('col-sm-6');
    posts.classList.add('col-lg-4');
    posts.classList.add('mb-4');

    postsbody.appendChild(postsh5);
    postsbody.appendChild(postsp1);
    postsbody.appendChild(postsp2);

    postscard.appendChild(postsbody);
    posts.appendChild(postscard);
    posts.classList.add('fade-in-box');
    posts.classList.add('result');
    

    mygallery.append(posts); //카드 생성

})
