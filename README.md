# 2023 유네스코 동아리 활동 팝콘 사전예약 프로젝트

<div><h2>사전예약 프로젝트란?</h2>
    <h4>고등학교 유네스코 동아리 활동에서 공공무역을 소개하기 위해서 팝콘을 판매하게 되었습니다.</h4>
    <h4>팝콘 판매대상은 고1, 고2 학생으로 약 300~400명 정도의 학생으로 타깃을 하고 프로젝트를 구상하게 되었습니다.</h4>
    <h4>하지만, 얼마나 많은 학생들이 부스에 방문해서 팝콘을 사게 될지 감이 안잡혔기 떄문에, 사전예약 프로젝트를 진행하게 되었습니다.</h4>
    <h4>축제 시작까지 8시간 남짓.. 제작부터 배포까지 해야하는 상황입니다.. 과연 전 할 수 있을까요? </h4>
</div>

<div><h2>어떻게 만들까 🤔</h2>
    <h4>저는 구상단계에서 가장 먼져 생각난것이 바코드였습니다.</h4>
    <h4>마침, 당근마켓에서 구매한 바코드 리더기가 있었기 떄문에, 쉽게 구현할 수 있을것 같았습니다!</h4>
    <h4>간단히 말로 설명하자면, DB에 [고객이름,전화번호,메뉴,입금은행,바코드번호] 이런식으로 구축을 하였습니다!</h4>
    <h4>이후, 바코드 스캐너로 찍으면 메뉴가 조회가 되고, 정상쿠폰인지 사용된 쿠폰인지 구분이 가능합니다.</h4>
</div>

<div><h2>바코드 테스트 😀</h2>
  <video width=30% src=https://github.com/jangwonjun/sdb_message/assets/41234293/1c7f516b-0cfc-4bf1-ad31-aebc5f78c766></video>
  <h5>자일리통에 있는 바코드 번호처럼 잘 스캔되는 모습을 보실수 있습니다.</h5>
</div>

<div><h2>DB 구성 😎</h2>
  <img width="524" alt="스크린샷 2023-12-26 오후 10 39 01" src="https://github.com/jangwonjun/sdb_message/assets/41234293/9dd06965-3c55-4944-b694-7fe5decc8263">
  <h4>개인정보로 인해서 모든 주문자분들의 정보를 보여드릴 수는 없지만, 1번 예시처럼 DB를 구성하였습니다.</h4>
</div>

<div><h2>바코드 생성하기 😱</h2>
  <h4>생각지도 못한 부분에서 난관에 봉착하였습니다.</h4>
  <h4>사실 파이썬에 python-barcode라는 pip가 있습니다만, 이것이 문제를 일으키던군요...</h4>
  <h4>import를 했지만, 라이브러리가 없다고 계속 출력되는 문제가 발생하였습니다.</h4>
  <h4>문제를 해결하고자, StackOverFlow을 뒤졌지만 외쿡인 분들도 안되는건 마찬가지더라구요..(황당)</h4>
  <h4>놀랍게도, 축제까지 남은 시간은 7시간전... 제일 좋은 방법은 쿠폰을 손수 만드는게 제일 편합니다 ㅎㅎ 노가다가 짱이지요~ </h4>
  <img src="https://github.com/jangwonjun/sdb_message/assets/41234293/4f8cdb10-5e7d-4c2f-a38a-6d32033347d4">
  <h4>이런식으로, 사전예약 하신 28분의 바코드를 생성하였습니다!</h4>
</div>

<div><h2>바코드 인식 프로그램 제작하기 🫡</h2>
  <img width="1257" alt="스크린샷 2023-12-26 오후 10 52 33" src="https://github.com/jangwonjun/sdb_message/assets/41234293/140d68e4-e052-4e18-805e-f0df558731cf">
  <h5>http://dev.activejang.kro.kr/search_code</h5>
  <h4>위에 링크에서 조회가 가능합니다!</h4>
  <h4>또한 인식후, 바코드 삭제하기를 눌러서 사용완료한 바코드라고 처리할 수 있습니다.</h4>
</div>

<div><h2>후기 - 성공적으로 마침</h2>
  <img src='https://github.com/jangwonjun/sdb_message/assets/41234293/2900b370-2a34-4b87-9aac-35fbc08922c5'>
  <video width=300px src=https://github.com/jangwonjun/sdb_message/assets/41234293/67a30f21-ee7a-4089-8bce-5e69afc95108></video>
  <h4>너무 시간이 적어서, UI/UX는 개나줘버리고 만든것이 없지 않아 있지만, 그걸 가만하면 잘 만들어진것 같은 프로그램인것 같습니다.</h4>
  <h4>실제로 팝콘 문자를 보낼떄에도 자동화를 하여서 전송하였기 때문에 잠자는 시간을 제외하고 약 2시간정도 만에 하나의 솔루션을 제작할 수 있었습니다.</h4>
  <h4>바코드 가지고 노는것이 생각보다 재미있기 때문에 다음에도 해보도록 하겠습니다 ㅋㅋㅋ</h4>
</div>