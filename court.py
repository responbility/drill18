from pico2d import load_image, get_canvas_width, get_canvas_height, clamp
import common

class Court:
    def __init__(self):
        # 맵 이미지 로드
        self.image = load_image('futsal_court.png')
        # 캔버스(윈도우) 크기
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        # 맵 전체 이미지의 너비/높이
        self.w = self.image.w
        self.h = self.image.h
        # 초기 윈도우 좌표
        self.window_left = 0
        self.window_bottom = 0


    def update(self):
        # 플레이어 중심으로 윈도우 왼쪽/아래 좌표를 계산
        # common.boy.x/y는 '실제' 맵 좌표(원점: 맵 왼쪽 아래)를 갖는다고 가정
        self.window_left = clamp(0, int(common.boy.x) - self.cw // 2, self.w - self.cw)
        self.window_bottom = clamp(0, int(common.boy.y) - self.ch // 2, self.h - self.ch)

    def draw(self):
        # 계산된 window_left/window_bottom에서 캔버스 크기(cw,ch)만큼 맵을 잘라서
        # 화면 원점(0,0)에 그립니다.
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)


class TileCourt:
    def __init__(self):
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        # 타일 방식은 실제 구현은 수업에 따라 다름. 기본값 초기화
        self.w = 0
        self.h = 0
        self.window_left = 0
        self.window_bottom = 0


    def update(self):
        pass

    def draw(self):
        # TileCourt의 경우에도 window 좌표 계산이 필요하면 여기서 수행
        self.window_left = clamp(0, int(common.boy.x) - self.cw // 2, max(0, self.w - self.cw))
        self.window_bottom = clamp(0, int(common.boy.y) - self.ch // 2, max(0, self.h - self.ch))


class InfiniteCourt:

    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        # quadrant 3: 우선 전체에서 잘라서 0,0에 그리는 부분
        self.image.clip_draw_to_origin(self.q3l, self.q3b, self.q3w, self.q3h, 0, 0)                        # quadrant 3
        # 추가 분할 영역(2,4,1)은 필요하면 계산하여 그립니다.

    def update(self):
        # quadrant 3
        self.q3l = (int(common.boy.x) - self.cw // 2) % self.w
        self.q3b = (int(common.boy.y) - self.ch // 2) % self.h
        self.q3w = clamp(0, self.w - self.q3l, self.w)
        self.q3h = clamp(0, self.h - self.q3b, self.h)
        # quadrant 2
        self.q2l = 0
        self.q2b = 0
        self.q2w = 0
        self.q2h = 0
        # quadrand 4
        self.q4l = 0
        self.q4b = 0
        self.q4w = 0
        self.q4h = 0
        # quadrand 1
        self.q1l = 0
        self.q1b = 0
        self.q1w = 0
        self.q1h = 0


    def handle_event(self, event):
        pass
