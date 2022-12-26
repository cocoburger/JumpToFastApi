from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# Base 클래스를 상속하며 만들어야 한다. __tablename__은 모델에 의해 관리되는 테이블의 이름을 뜻한다.
# Column() 괄호 안의 첫 번째 인수는 데이터 타입을 의미한다. 데이터 타입은 속성에 저장할 데이터의 종류를 결정한다.
# Integer는 고유 번호와 같은 숫자값에 사용하고, String은 제목처럼 글자 수가 제한된 텓스트에 사용한다. 글 내용처럼 글자 수를 제한
# 할 수 없는 텍스트는 Text를 사용한다. 작성일시는 날짜 타입인 DateTime을 사용했다.

# primary_key : id 속성에 설정한 primary_key는 id속성을 기본 키로 만든다.
# 기본 키는 데이터베이스에서 중복된 값을 가잘 수 없게 만드는 설정이다.
# id는 모델에서 각 데이터를 구분하는 유일한 값이므로 중복되면 안되므로 기본키로 지정했다.

# nullable : null값을 허용할지의 여부이다. nullable을 따로 설정하지 않으면 해당 속성은 기본으로 null값을 허용한다.
# null값을 허용하지 않으려면 nullable=False로 설정해야 한다.


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)


# question_id 속성은 답변을 질문과 연결하기 위해 추가된 속성이다. 답변은 어떤 질문에 대한 답변인지 알아야 하므로 질문의 id속성이 필요하다.
# 그리고 모델을 서로 연결할 떄에는 위와 같이 ForeignKey를 사용해야 한다.
# 데이터베이스에서는 기존 모델과 연결된 속성을 외부 키(Foreign Key)라고 한다.
# ForeginKey의 첫 번째 파라미터 'question_id'속성은 question 테이블의 id 컬럼과 연결된다는 뜻이다.
class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")
