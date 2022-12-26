from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db" # 데이터 베이스 접속 주소


# 커넥션 풀을 생성한다. 커넥션 풀이란 데이터베이스에 접속하는 객체를 일정 갯수만큼 만들어 놓고 돌려가며 사용하는 것을 말한다.
# db에 접속하는 세션 수를 제어하고, 또 세션 접속에 소요되는 시간을 줄이고자 하는 용도로 사용한다.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

# 데이터베이스에 접속하기 위해 필요한 클래스이다. create_engine, sessionmaker등을 사용하는 것은
# SQLAlchemy 데이터베이스를 사용하기 위해 따라야 할 규칙이다. 정해진 규칙대로 사용하면 되지만 여기서 autocommit=False부분은 주의하자
# 해당 설정값이 True인 경우 commit이라는 사인이 없어도 즉시 db에 변경사항이 적용된다.
# False인 경우에는 데이터를 잘못 저장했을 경우 rollback 사인으로 되돌리는 것이 가능하지만 True인 경우에는 commit이 필요없는 것처럼
# rollback도 동작하지 않는다는 점을 주의하자
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 반환된 Base 클래스는 db 모델을 구성할 때 사용되는 클래스이다.
Base = declarative_base()


# SQLite : 파이썬 기본 패키지에 포함된 SQLite는 주로 소규모 프로젝트에서 사용하는 가벼운 파일을 기반으로 한 db다.
# 보통은 SQLite로 개발을 빠르게 진행하고 이후 실제 운영 시스템에 반영할 때에는 좀 더 규모가 큰 db로 교체한다.

