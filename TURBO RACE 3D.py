import sys
import math
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                              QHBoxLayout, QPushButton, QLabel, QComboBox,
                              QSlider, QFrame, QSizePolicy, QGridLayout,
                              QProgressBar, QSpacerItem)
from PyQt6.QtCore import (Qt, QTimer, QPoint, QRect, QSize, pyqtSignal,
                           QPropertyAnimation, QEasingCurve, QThread, QObject)
from PyQt6.QtGui import (QPainter, QColor, QFont, QBrush, QPen, QLinearGradient,
                          QRadialGradient, QPainterPath, QPolygon, QTransform,
                          QFontMetrics, QPixmap, QImage, QPalette)


TRANSLATIONS = {
    "en": {
        "title": "TURBO RACE 3D",
        "start": "START RACE",
        "pause": "PAUSE",
        "resume": "RESUME",
        "restart": "RESTART",
        "speed": "SPEED",
        "lap": "LAP",
        "time": "TIME",
        "best": "BEST LAP",
        "position": "POSITION",
        "score": "SCORE",
        "game_over": "RACE FINISHED!",
        "play_again": "PLAY AGAIN",
        "settings": "SETTINGS",
        "language": "Language",
        "theme": "Theme",
        "dark": "Dark",
        "light": "Light",
        "difficulty": "Difficulty",
        "easy": "Easy",
        "medium": "Medium",
        "hard": "Hard",
        "sound": "Sound",
        "controls": "Controls: Arrow Keys / WASD",
        "nitro": "NITRO",
        "mph": "MPH",
        "laps_of": "of",
        "total_laps": "TOTAL LAPS",
        "rank": "RANK",
    },
    "fa": {
        "title": "مسابقه توربو ۳D",
        "start": "شروع مسابقه",
        "pause": "توقف",
        "resume": "ادامه",
        "restart": "شروع مجدد",
        "speed": "سرعت",
        "lap": "دور",
        "time": "زمان",
        "best": "بهترین دور",
        "position": "موقعیت",
        "score": "امتیاز",
        "game_over": "مسابقه تمام شد!",
        "play_again": "بازی مجدد",
        "settings": "تنظیمات",
        "language": "زبان",
        "theme": "پوسته",
        "dark": "تاریک",
        "light": "روشن",
        "difficulty": "سختی",
        "easy": "آسان",
        "medium": "متوسط",
        "hard": "سخت",
        "sound": "صدا",
        "controls": "کنترل: کلیدهای جهتی / WASD",
        "nitro": "نیترو",
        "mph": "کمپه",
        "laps_of": "از",
        "total_laps": "کل دورها",
        "rank": "رتبه",
    },
    "zh": {
        "title": "涡轮竞速 3D",
        "start": "开始比赛",
        "pause": "暂停",
        "resume": "继续",
        "restart": "重新开始",
        "speed": "速度",
        "lap": "圈数",
        "time": "时间",
        "best": "最佳圈速",
        "position": "位置",
        "score": "分数",
        "game_over": "比赛结束！",
        "play_again": "再玩一次",
        "settings": "设置",
        "language": "语言",
        "theme": "主题",
        "dark": "深色",
        "light": "浅色",
        "difficulty": "难度",
        "easy": "简单",
        "medium": "中等",
        "hard": "困难",
        "sound": "声音",
        "controls": "控制: 方向键 / WASD",
        "nitro": "氮气",
        "mph": "英里/时",
        "laps_of": "共",
        "total_laps": "总圈数",
        "rank": "排名",
    }
}

DARK_THEME = {
    "bg": "#0a0a0f",
    "bg2": "#12121e",
    "bg3": "#1a1a2e",
    "panel": "#16213e",
    "panel2": "#0f3460",
    "accent": "#e94560",
    "accent2": "#f5a623",
    "accent3": "#00d4ff",
    "text": "#ffffff",
    "text2": "#b0b8d8",
    "text3": "#6a7299",
    "border": "#2a2a4a",
    "border2": "#e94560",
    "button_bg": "#e94560",
    "button_text": "#ffffff",
    "button_hover": "#ff6b7a",
    "nitro_bar": "#00d4ff",
    "speed_bar": "#f5a623",
    "health_bar": "#00ff7f",
    "road": "#1c1c2e",
    "road_line": "#f5a623",
    "sky_top": "#0a0a1a",
    "sky_bottom": "#1a0a2e",
    "grass": "#0a1a0a",
    "car_body": "#e94560",
    "car_roof": "#c73350",
    "car_wheel": "#2a2a2a",
    "car_window": "#00d4ff",
    "shadow": "#00000080",
    "glow": "#e9456040",
    "hud_bg": "#0a0a1480",
    "hud_border": "#e9456060",
    "track_bg": "#0f3460",
    "neon1": "#ff00ff",
    "neon2": "#00ffff",
    "star": "#ffffff",
}

LIGHT_THEME = {
    "bg": "#e8f0fe",
    "bg2": "#dce8ff",
    "bg3": "#c8daff",
    "panel": "#ffffff",
    "panel2": "#f0f4ff",
    "accent": "#1a73e8",
    "accent2": "#ea4335",
    "accent3": "#34a853",
    "text": "#1a1a2e",
    "text2": "#3a3a5e",
    "text3": "#6a6a9e",
    "border": "#c0cce8",
    "border2": "#1a73e8",
    "button_bg": "#1a73e8",
    "button_text": "#ffffff",
    "button_hover": "#1557b0",
    "nitro_bar": "#34a853",
    "speed_bar": "#ea4335",
    "health_bar": "#34a853",
    "road": "#4a4a6a",
    "road_line": "#ffffff",
    "sky_top": "#1a6eb5",
    "sky_bottom": "#87ceeb",
    "grass": "#2d7a2d",
    "car_body": "#1a73e8",
    "car_roof": "#0d47a1",
    "car_wheel": "#1a1a1a",
    "car_window": "#87ceeb",
    "shadow": "#00000040",
    "glow": "#1a73e840",
    "hud_bg": "#ffffff99",
    "hud_border": "#1a73e880",
    "track_bg": "#c8daff",
    "neon1": "#1a73e8",
    "neon2": "#ea4335",
    "star": "#1a1a2e",
}


class Road:
    def __init__(self):
        self.segments = []
        self.track_length = 200
        self.curve_strength = 0
        self.hills = []
        self._generate_track()

    def _generate_track(self):
        self.segments = []
        for i in range(self.track_length):
            seg = {
                "index": i,
                "curve": 0.0,
                "y": 0.0,
                "color_flip": i % 2 == 0,
            }
            if i > 10 and i < 50:
                seg["curve"] = 2.5
            elif i > 60 and i < 100:
                seg["curve"] = -3.0
            elif i > 120 and i < 160:
                seg["curve"] = 1.8
            if i > 30 and i < 70:
                seg["y"] = math.sin((i - 30) * 0.1) * 30
            self.segments.append(seg)

    def get_segment(self, pos):
        idx = int(pos) % self.track_length
        return self.segments[idx]


class AIOpponent:
    def __init__(self, oid, color, speed_factor):
        self.id = oid
        self.color = color
        self.position = random.uniform(20, 80)
        self.speed = 0
        self.max_speed = 180 * speed_factor
        self.acceleration = 1.2 * speed_factor
        self.lap = 0
        self.total_distance = 0
        self.x_offset = random.uniform(-0.3, 0.3)
        self.wobble = 0
        self.wobble_dir = random.choice([-1, 1])

    def update(self, dt, difficulty):
        target_speed = self.max_speed
        if difficulty == "easy":
            target_speed *= 0.7
        elif difficulty == "hard":
            target_speed *= 1.1
        if self.speed < target_speed:
            self.speed = min(self.speed + self.acceleration, target_speed)
        self.total_distance += self.speed * dt * 0.01
        self.wobble += 0.05 * self.wobble_dir
        if abs(self.wobble) > 0.15:
            self.wobble_dir *= -1


class GameState:
    def __init__(self, total_laps=3, difficulty="medium"):
        self.total_laps = total_laps
        self.difficulty = difficulty
        self.reset()

    def reset(self):
        self.player_pos = 0.0
        self.player_speed = 0.0
        self.player_lap = 0
        self.player_x = 0.0
        self.player_total = 0.0
        self.max_speed = 220.0
        self.acceleration = 2.5
        self.braking = 5.0
        self.friction = 0.95
        self.steering = 0.0
        self.nitro = 100.0
        self.nitro_active = False
        self.nitro_cooldown = 0
        self.lap_time = 0.0
        self.total_time = 0.0
        self.best_lap = None
        self.lap_start = 0.0
        self.score = 0
        self.finished = False
        self.camera_depth = 0.84
        self.camera_height = 1500
        self.draw_length = 200
        self.fog_density = 5
        self.keys = {
            Qt.Key.Key_Up: False, Qt.Key.Key_Down: False,
            Qt.Key.Key_Left: False, Qt.Key.Key_Right: False,
            Qt.Key.Key_W: False, Qt.Key.Key_S: False,
            Qt.Key.Key_A: False, Qt.Key.Key_D: False,
            Qt.Key.Key_Space: False,
        }
        self.opponents = [
            AIOpponent(0, "#ff6b35", 0.82),
            AIOpponent(1, "#7b2fff", 0.88),
            AIOpponent(2, "#00c896", 0.91),
        ]
        for i, op in enumerate(self.opponents):
            op.total_distance = i * 5


class RaceCanvas(QWidget):
    def __init__(self, game_state, theme, parent=None):
        super().__init__(parent)
        self.game_state = game_state
        self.theme = theme
        self.road = Road()
        self.setMinimumSize(400, 300)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self._stars = [(random.uniform(0, 1), random.uniform(0, 0.5), random.uniform(0.5, 2.5))
                       for _ in range(80)]
        self._particles = []
        self._trail = []
        self._frame = 0
        self._skid_marks = []

    def set_theme(self, theme):
        self.theme = theme
        self.update()

    def sizeHint(self):
        return QSize(800, 500)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        w, h = self.width(), self.height()
        self._frame += 1
        self._draw_sky(p, w, h)
        self._draw_road_3d(p, w, h)
        self._draw_player_car(p, w, h)
        self._draw_particles(p, w, h)
        p.end()

    def _draw_sky(self, p, w, h):
        horizon = int(h * 0.42)
        grad = QLinearGradient(0, 0, 0, horizon)
        grad.setColorAt(0, QColor(self.theme["sky_top"]))
        grad.setColorAt(1, QColor(self.theme["sky_bottom"]))
        p.fillRect(0, 0, w, horizon, grad)

        star_color = QColor(self.theme["star"])
        for sx, sy, sr in self._stars:
            px = int(sx * w)
            py = int(sy * horizon)
            twinkle = 0.5 + 0.5 * math.sin(self._frame * 0.04 + sx * 10)
            star_color.setAlphaF(twinkle * 0.9 + 0.1)
            p.setPen(Qt.PenStyle.NoPen)
            p.setBrush(QBrush(star_color))
            r = sr * (0.7 + 0.3 * twinkle)
            p.drawEllipse(px, py, int(r * (w / 800)), int(r * (h / 500)))

        sun_x = int(w * 0.72)
        sun_y = int(horizon * 0.38)
        sun_r = int(min(w, h) * 0.045)
        sgr = QRadialGradient(sun_x, sun_y, sun_r * 2.5)
        sgr.setColorAt(0, QColor(self.theme["accent2"] + "ff"))
        sgr.setColorAt(0.4, QColor(self.theme["accent2"] + "aa"))
        sgr.setColorAt(1, QColor(self.theme["accent2"] + "00"))
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QBrush(sgr))
        p.drawEllipse(sun_x - sun_r * 2, sun_y - sun_r * 2, sun_r * 5, sun_r * 5)

        p.setBrush(QBrush(QColor(self.theme["accent2"] + "ee")))
        p.drawEllipse(sun_x - sun_r, sun_y - sun_r, sun_r * 2, sun_r * 2)

        grad2 = QLinearGradient(0, horizon - 2, 0, horizon + 10)
        grad2.setColorAt(0, QColor(self.theme["accent3"] + "44"))
        grad2.setColorAt(1, QColor(self.theme["accent3"] + "00"))
        p.fillRect(0, horizon - 2, w, 12, grad2)

    def _draw_road_3d(self, p, w, h):
        gs = self.game_state
        road = self.road
        segments = road.segments
        track_len = road.track_length

        horizon = int(h * 0.42)
        road_w = w * 0.55
        cam_depth = gs.camera_depth
        cam_height = gs.camera_height
        draw_len = min(gs.draw_length, track_len - 1)

        start_pos = int(gs.player_pos)
        x = 0.0
        max_y = h

        grass_colors = [QColor(self.theme["grass"]), QColor(self.theme["grass"]).lighter(115)]
        road_colors = [QColor(self.theme["road"]), QColor(self.theme["road"]).lighter(108)]
        rumble_colors = [QColor(self.theme["accent"]), QColor(self.theme["road_line"])]
        line_color = QColor(self.theme["road_line"])

        proj_cache = []
        for n in range(draw_len):
            idx = (start_pos + n) % track_len
            seg = segments[idx]
            scale = cam_depth / (n + cam_depth)
            proj_x = int(w / 2 + scale * x * road_w)
            proj_y = int(horizon + scale * cam_height)
            proj_w = int(scale * road_w)
            proj_cache.append((proj_x, proj_y, proj_w, seg, scale, n))
            if n > 0:
                x += seg["curve"] * 0.001 * scale

        for i in range(len(proj_cache) - 1, 0, -1):
            curr = proj_cache[i]
            prev = proj_cache[i - 1]
            cx, cy, cw, cseg, cs, cn = curr
            px, py, pw, pseg, ps, pn = prev

            if cy >= max_y or py >= max_y:
                continue
            if cy > py:
                continue

            flip = cseg["color_flip"]
            gc = grass_colors[1 if flip else 0]
            p.fillRect(0, cy, w, py - cy, gc)

            rc = road_colors[1 if flip else 0]
            road_pts = QPolygon([
                QPoint(px - pw, py), QPoint(px + pw, py),
                QPoint(cx + cw, cy), QPoint(cx - cw, cy)
            ])
            p.setPen(Qt.PenStyle.NoPen)
            p.setBrush(QBrush(rc))
            p.drawPolygon(road_pts)

            rumble_w = int(pw * 0.12)
            rcolor = rumble_colors[1 if flip else 0]
            p.setBrush(QBrush(rcolor))
            lpts = QPolygon([
                QPoint(px - pw, py), QPoint(px - pw + rumble_w, py),
                QPoint(cx - cw + rumble_w, cy), QPoint(cx - cw, cy)
            ])
            p.drawPolygon(lpts)
            rpts = QPolygon([
                QPoint(px + pw - rumble_w, py), QPoint(px + pw, py),
                QPoint(cx + cw, cy), QPoint(cx + cw - rumble_w, cy)
            ])
            p.drawPolygon(rpts)

            if flip:
                center_w = int(pw * 0.05)
                p.setBrush(QBrush(line_color))
                cpts = QPolygon([
                    QPoint(px - center_w, py), QPoint(px + center_w, py),
                    QPoint(cx + center_w, cy), QPoint(cx - center_w, cy)
                ])
                p.drawPolygon(cpts)

            for opp in gs.opponents:
                opp_dist = opp.total_distance % track_len
                player_dist = gs.player_total % track_len
                diff = opp_dist - player_dist
                if int(diff) == pn:
                    ox = int(px + opp.x_offset * pw * 1.5)
                    car_h = int((py - cy) * 3.5)
                    car_w = int(car_h * 0.55)
                    self._draw_ai_car(p, ox, py - car_h, car_w, car_h, opp.color, cs)

            max_y = cy

        p.fillRect(0, 0, w, horizon, QColor(self.theme["sky_bottom"] + "00"))

    def _draw_ai_car(self, p, x, y, car_w, car_h, color, scale):
        if car_w < 4 or car_h < 4:
            return
        body_color = QColor(color)
        roof_color = body_color.darker(130)
        wheel_color = QColor(self.theme["car_wheel"])
        win_color = QColor(self.theme["car_window"])

        bx = x - car_w // 2
        by = y + int(car_h * 0.4)
        bw = car_w
        bh = int(car_h * 0.45)
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QBrush(body_color))
        p.drawRoundedRect(bx, by, bw, bh, 3, 3)

        rw = int(bw * 0.72)
        rh = int(car_h * 0.35)
        rx = bx + (bw - rw) // 2
        ry = by - rh + 4
        p.setBrush(QBrush(roof_color))
        p.drawRoundedRect(rx, ry, rw, rh, 4, 4)

        ww = max(3, int(car_w * 0.22))
        wh = max(4, int(car_h * 0.22))
        p.setBrush(QBrush(wheel_color))
        for wx, wy in [(bx - ww // 2, by + bh - wh // 2),
                       (bx + bw - ww // 2, by + bh - wh // 2)]:
            p.drawEllipse(wx, wy, ww, wh)

        if rw > 10:
            p.setBrush(QBrush(win_color.lighter(120)))
            p.setOpacity(0.65)
            p.drawRoundedRect(rx + 3, ry + 3, rw - 6, rh - 6, 3, 3)
            p.setOpacity(1.0)

    def _draw_player_car(self, p, w, h):
        gs = self.game_state
        speed_ratio = gs.player_speed / gs.max_speed

        cx = w // 2
        cy = int(h * 0.82)
        car_w = int(min(w, h) * 0.18)
        car_h = int(car_w * 0.52)

        shadow_color = QColor(self.theme["shadow"])
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QBrush(shadow_color))
        p.drawEllipse(cx - car_w // 2 - 5, cy + car_h - 8, car_w + 10, 14)

        if gs.nitro_active and gs.nitro > 0:
            for i in range(3):
                glow_r = car_w * (0.8 + i * 0.3)
                glow_color = QColor(self.theme["nitro_bar"])
                glow_color.setAlphaF(0.15 - i * 0.04)
                p.setBrush(QBrush(glow_color))
                p.drawEllipse(int(cx - glow_r / 2), int(cy - glow_r * 0.3),
                               int(glow_r), int(glow_r * 0.6))

        body_color = QColor(self.theme["car_body"])
        roof_color = QColor(self.theme["car_roof"])
        wheel_color = QColor(self.theme["car_wheel"])
        win_color = QColor(self.theme["car_window"])
        accent_c = QColor(self.theme["accent2"])

        bx = cx - car_w // 2
        by = cy - car_h // 2
        bw = car_w
        bh = int(car_h * 0.55)
        body_grad = QLinearGradient(bx, by, bx + bw, by + bh)
        body_grad.setColorAt(0, body_color.lighter(130))
        body_grad.setColorAt(0.5, body_color)
        body_grad.setColorAt(1, body_color.darker(120))
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QBrush(body_grad))
        p.drawRoundedRect(bx, by + int(car_h * 0.35), bw, bh, 6, 6)

        rw = int(bw * 0.68)
        rh = int(car_h * 0.42)
        rx = bx + (bw - rw) // 2
        ry = by + int(car_h * 0.05)
        roof_grad = QLinearGradient(rx, ry, rx + rw, ry + rh)
        roof_grad.setColorAt(0, roof_color.lighter(115))
        roof_grad.setColorAt(1, roof_color.darker(115))
        p.setBrush(QBrush(roof_grad))
        p.drawRoundedRect(rx, ry, rw, rh, 8, 8)

        p.setBrush(QBrush(win_color))
        p.setOpacity(0.75)
        p.drawRoundedRect(rx + 5, ry + 5, rw - 10, int(rh * 0.72), 5, 5)
        p.setOpacity(1.0)

        p.setBrush(QBrush(QColor(self.theme["star"] + "88")))
        p.setOpacity(0.35)
        p.drawRect(rx + 8, ry + 7, int((rw - 16) * 0.45), rh // 4)
        p.setOpacity(1.0)

        ww = int(car_w * 0.2)
        wh = int(car_h * 0.28)
        wheel_angle = self._frame * (speed_ratio * 15)
        for wpos in [(bx - ww + 6, by + int(car_h * 0.72)),
                     (bx + bw - 6, by + int(car_h * 0.72)),
                     (bx - ww + 6, by + int(car_h * 0.35)),
                     (bx + bw - 6, by + int(car_h * 0.35))]:
            wx, wy = wpos
            wg = QRadialGradient(wx + ww // 2, wy + wh // 2, ww // 2)
            wg.setColorAt(0, wheel_color.lighter(150))
            wg.setColorAt(0.4, wheel_color)
            wg.setColorAt(1, QColor("#000000"))
            p.setBrush(QBrush(wg))
            p.drawEllipse(wx, wy, ww, wh)
            p.setPen(QPen(QColor(self.theme["accent2"]), 1))
            spoke_cx = wx + ww // 2
            spoke_cy = wy + wh // 2
            for sp in range(4):
                ang = math.radians(wheel_angle + sp * 45)
                sx = spoke_cx + int(math.cos(ang) * (ww // 2 - 2))
                sy = spoke_cy + int(math.sin(ang) * (wh // 2 - 2))
                p.drawLine(spoke_cx, spoke_cy, sx, sy)
            p.setPen(Qt.PenStyle.NoPen)

        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QBrush(accent_c))
        hl_w = int(car_w * 0.12)
        hl_h = int(car_h * 0.1)
        for hx in [bx + 4, bx + bw - hl_w - 4]:
            p.drawRoundedRect(hx, by + int(car_h * 0.85), hl_w, hl_h, 2, 2)
            ghl = QRadialGradient(hx + hl_w // 2, by + int(car_h * 0.85) + hl_h // 2,
                                   hl_w * 0.9)
            ghl.setColorAt(0, QColor(self.theme["accent2"] + "cc"))
            ghl.setColorAt(1, QColor(self.theme["accent2"] + "00"))
            p.setBrush(QBrush(ghl))
            p.drawEllipse(hx - hl_w // 2, by + int(car_h * 0.8),
                           hl_w * 2, hl_h * 2)

        tail_color = QColor("#ff3333") if speed_ratio < 0.1 else QColor("#660000")
        p.setBrush(QBrush(tail_color))
        tl_w = int(car_w * 0.14)
        tl_h = int(car_h * 0.09)
        for tx_offset in [bx + 6, bx + bw - tl_w - 6]:
            p.drawRoundedRect(tx_offset, by + int(car_h * 0.38), tl_w, tl_h, 2, 2)

        if gs.nitro_active and gs.nitro > 0:
            exhaust_x = cx - 8
            exhaust_y = by + int(car_h * 0.42)
            for i in range(5):
                flame_len = random.randint(8, 22) * (1 + speed_ratio)
                fw = random.randint(4, 9)
                fc = QColor(self.theme["nitro_bar"])
                fc.setAlphaF(0.8 - i * 0.15)
                p.setBrush(QBrush(fc))
                p.drawEllipse(int(exhaust_x - fw // 2 + random.randint(-2, 2)),
                               int(exhaust_y + i * 3),
                               fw, int(flame_len * 0.4))

        if speed_ratio > 0.5:
            for _ in range(int(speed_ratio * 3)):
                px2 = cx + random.randint(-car_w // 2, car_w // 2)
                py2 = by + car_h + random.randint(0, 15)
                self._particles.append({
                    "x": px2, "y": py2,
                    "vx": random.uniform(-1.5, 1.5),
                    "vy": random.uniform(1, 4),
                    "life": 1.0,
                    "color": self.theme["accent"] if not gs.nitro_active else self.theme["nitro_bar"]
                })

    def _draw_particles(self, p, w, h):
        alive = []
        for pt in self._particles:
            pt["x"] += pt["vx"]
            pt["y"] += pt["vy"]
            pt["life"] -= 0.06
            if pt["life"] > 0:
                pc = QColor(pt["color"])
                pc.setAlphaF(pt["life"] * 0.6)
                p.setPen(Qt.PenStyle.NoPen)
                p.setBrush(QBrush(pc))
                r = max(1, int(pt["life"] * 4))
                p.drawEllipse(int(pt["x"]) - r, int(pt["y"]) - r, r * 2, r * 2)
                alive.append(pt)
        self._particles = alive[-80:]

    def keyPressEvent(self, event):
        key = event.key()
        if key in self.game_state.keys:
            self.game_state.keys[key] = True

    def keyReleaseEvent(self, event):
        key = event.key()
        if key in self.game_state.keys:
            self.game_state.keys[key] = False


class HUDWidget(QWidget):
    def __init__(self, game_state, theme, lang, parent=None):
        super().__init__(parent)
        self.game_state = game_state
        self.theme = theme
        self.lang = lang
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setMinimumHeight(100)

    def set_theme(self, theme):
        self.theme = theme
        self.update()

    def set_lang(self, lang):
        self.lang = lang
        self.update()

    def tr(self, key):
        return TRANSLATIONS[self.lang].get(key, key)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        w, h = self.width(), self.height()
        gs = self.game_state

        unit = min(w, h * 3)
        font_big = max(10, int(unit * 0.04))
        font_med = max(8, int(unit * 0.027))
        font_sm = max(7, int(unit * 0.022))

        panel_h = int(h * 0.88)
        panel_w = int(w * 0.28)
        panel_w = max(120, min(panel_w, 240))

        self._draw_panel(p, 8, 8, panel_w, panel_h, gs, font_big, font_med, font_sm, w, h)
        self._draw_right_panel(p, w - panel_w - 8, 8, panel_w, panel_h, gs, font_med, font_sm)
        self._draw_speed_meter(p, w, h, gs, font_big, font_med)

        p.end()

    def _draw_panel(self, p, px, py, pw, ph, gs, fb, fm, fs, w, h):
        t = self.theme
        bg = QColor(t["hud_bg"])
        border = QColor(t["hud_border"])
        text_c = QColor(t["text"])
        text2_c = QColor(t["text2"])
        accent = QColor(t["accent"])
        accent2 = QColor(t["accent2"])
        accent3 = QColor(t["accent3"])

        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QBrush(bg))
        p.drawRoundedRect(px, py, pw, ph, 12, 12)
        p.setPen(QPen(border, 1.5))
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawRoundedRect(px, py, pw, ph, 12, 12)

        y = py + 14
        items = [
            (self.tr("lap"), f"{gs.player_lap}/{gs.total_laps}", accent),
            (self.tr("time"), self._fmt_time(gs.total_time), text_c),
            (self.tr("best"), self._fmt_time(gs.best_lap) if gs.best_lap else "--:--.--", accent2),
            (self.tr("score"), str(int(gs.score)), accent3),
        ]
        for label, val, vc in items:
            p.setPen(QPen(text2_c))
            p.setFont(QFont("Arial", fs, QFont.Weight.Normal))
            p.drawText(px + 10, y, pw - 14, 16, Qt.AlignmentFlag.AlignLeft, label.upper())
            y += 14
            p.setPen(QPen(vc))
            p.setFont(QFont("Arial", fm, QFont.Weight.Bold))
            p.drawText(px + 10, y, pw - 14, 20, Qt.AlignmentFlag.AlignLeft, val)
            y += 22

        y += 6
        p.setPen(QPen(text2_c))
        p.setFont(QFont("Arial", fs))
        p.drawText(px + 10, y, pw - 14, 16, Qt.AlignmentFlag.AlignLeft,
                   self.tr("nitro").upper())
        y += 14
        self._draw_bar(p, px + 10, y, pw - 20, 10,
                       gs.nitro / 100, QColor(t["nitro_bar"]), QColor(t["border"]))
        y += 18

    def _draw_right_panel(self, p, px, py, pw, ph, gs, fm, fs):
        t = self.theme
        bg = QColor(t["hud_bg"])
        border = QColor(t["hud_border"])
        text2_c = QColor(t["text2"])
        accent = QColor(t["accent"])
        accent2 = QColor(t["accent2"])

        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QBrush(bg))
        p.drawRoundedRect(px, py, pw, ph, 12, 12)
        p.setPen(QPen(border, 1.5))
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawRoundedRect(px, py, pw, ph, 12, 12)

        y = py + 14
        p.setPen(QPen(text2_c))
        p.setFont(QFont("Arial", fs))
        p.drawText(px + 10, y, pw - 14, 16, Qt.AlignmentFlag.AlignLeft,
                   self.tr("rank").upper())
        y += 14

        all_racers = [(gs.player_total, "YOU", QColor(t["accent"]))] + \
                     [(op.total_distance, f"AI {op.id + 1}", QColor(op.color))
                      for op in gs.opponents]
        all_racers.sort(key=lambda x: -x[0])

        for i, (dist, name, color) in enumerate(all_racers):
            p.setPen(QPen(color))
            p.setFont(QFont("Arial", fs, QFont.Weight.Bold))
            p.drawText(px + 10, y, pw - 14, 18,
                       Qt.AlignmentFlag.AlignLeft, f"{i + 1}. {name}")
            y += 18

    def _draw_speed_meter(self, p, w, h, gs, fb, fm):
        t = self.theme
        cx = w // 2
        cy = h - int(h * 0.04)
        radius = int(min(w * 0.07, h * 0.22))
        radius = max(32, min(radius, 80))

        bg = QColor(t["hud_bg"])
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QBrush(bg))
        p.drawEllipse(cx - radius - 10, cy - radius * 2 - 10,
                      radius * 2 + 20, radius * 2 + 20)

        border = QColor(t["hud_border"])
        p.setPen(QPen(border, 1.5))
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawEllipse(cx - radius - 10, cy - radius * 2 - 10,
                      radius * 2 + 20, radius * 2 + 20)

        arc_rect = QRect(cx - radius, cy - radius * 2, radius * 2, radius * 2)
        speed_ratio = gs.player_speed / gs.max_speed

        p.setPen(QPen(QColor(t["border"]), int(radius * 0.14), Qt.PenStyle.SolidLine,
                       Qt.PenCapStyle.RoundCap))
        p.drawArc(arc_rect, 30 * 16, 120 * 16)

        if speed_ratio > 0:
            bar_color = QColor(t["speed_bar"])
            if speed_ratio > 0.85:
                bar_color = QColor(t["accent"])
            p.setPen(QPen(bar_color, int(radius * 0.14), Qt.PenStyle.SolidLine,
                           Qt.PenCapStyle.RoundCap))
            p.drawArc(arc_rect, 30 * 16, int(120 * 16 * speed_ratio))

        speed_val = int(gs.player_speed)
        p.setPen(QPen(QColor(t["text"])))
        p.setFont(QFont("Arial", fb, QFont.Weight.Bold))
        p.drawText(cx - radius, cy - radius * 2 + 10, radius * 2, radius * 2 - 10,
                   Qt.AlignmentFlag.AlignCenter, str(speed_val))
        p.setFont(QFont("Arial", max(7, int(fb * 0.55))))
        p.setPen(QPen(QColor(t["text2"])))
        p.drawText(cx - radius, cy - radius * 2 + 10, radius * 2, radius * 2 + 20,
                   Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom,
                   self.tr("mph"))

    def _draw_bar(self, p, x, y, w, h, ratio, fill_color, bg_color):
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QBrush(bg_color))
        p.drawRoundedRect(x, y, w, h, h // 2, h // 2)
        if ratio > 0:
            fc = QColor(fill_color)
            grad = QLinearGradient(x, y, x + int(w * ratio), y)
            grad.setColorAt(0, fc.lighter(130))
            grad.setColorAt(1, fc)
            p.setBrush(QBrush(grad))
            p.drawRoundedRect(x, y, int(w * ratio), h, h // 2, h // 2)

    def _fmt_time(self, t):
        if t is None:
            return "--:--.--"
        mins = int(t) // 60
        secs = int(t) % 60
        ms = int((t - int(t)) * 100)
        return f"{mins:02d}:{secs:02d}.{ms:02d}"


class GameOverOverlay(QWidget):
    play_again = pyqtSignal()
    back_menu = pyqtSignal()

    def __init__(self, game_state, theme, lang, parent=None):
        super().__init__(parent)
        self.game_state = game_state
        self.theme = theme
        self.lang = lang
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def tr(self, key):
        return TRANSLATIONS[self.lang].get(key, key)

    def set_theme(self, theme):
        self.theme = theme
        self.update()

    def set_lang(self, lang):
        self.lang = lang
        self.update()

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        w, h = self.width(), self.height()
        t = self.theme

        overlay = QColor(t["bg"])
        overlay.setAlphaF(0.87)
        p.fillRect(0, 0, w, h, overlay)

        bw = min(int(w * 0.55), 420)
        bh = min(int(h * 0.62), 360)
        bx = (w - bw) // 2
        by = (h - bh) // 2

        bg = QColor(t["panel"])
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QBrush(bg))
        p.drawRoundedRect(bx, by, bw, bh, 18, 18)

        border = QColor(t["accent"])
        p.setPen(QPen(border, 2))
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawRoundedRect(bx, by, bw, bh, 18, 18)

        title_fs = max(14, int(min(w, h) * 0.042))
        p.setFont(QFont("Arial", title_fs, QFont.Weight.Bold))
        p.setPen(QPen(QColor(t["accent"])))
        p.drawText(bx, by + 20, bw, 50, Qt.AlignmentFlag.AlignCenter, self.tr("game_over"))

        gs = self.game_state
        info_fs = max(10, int(title_fs * 0.6))
        p.setFont(QFont("Arial", info_fs))
        p.setPen(QPen(QColor(t["text"])))
        iy = by + 85
        for label, val in [
            (self.tr("score"), str(int(gs.score))),
            (self.tr("time"), self._fmt(gs.total_time)),
            (self.tr("best"), self._fmt(gs.best_lap) if gs.best_lap else "--"),
        ]:
            p.drawText(bx + 30, iy, bw - 60, 28,
                       Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
                       label + ":")
            p.setPen(QPen(QColor(t["accent2"])))
            p.drawText(bx + 30, iy, bw - 60, 28,
                       Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
                       val)
            p.setPen(QPen(QColor(t["text"])))
            iy += 32
        p.end()

    def _fmt(self, t):
        if not t:
            return "--"
        mins = int(t) // 60
        secs = int(t) % 60
        ms = int((t - int(t)) * 100)
        return f"{mins:02d}:{secs:02d}.{ms:02d}"


class ControlBar(QWidget):
    start_clicked = pyqtSignal()
    pause_clicked = pyqtSignal()
    restart_clicked = pyqtSignal()
    theme_changed = pyqtSignal(str)
    lang_changed = pyqtSignal(str)

    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.lang = lang
        self._running = False
        self._paused = False
        self._setup_ui()

    def _setup_ui(self):
        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(12, 6, 12, 6)
        self._layout.setSpacing(10)

        self.btn_start = QPushButton()
        self.btn_pause = QPushButton()
        self.btn_restart = QPushButton()

        for btn in [self.btn_start, self.btn_pause, self.btn_restart]:
            btn.setMinimumHeight(36)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.btn_pause.setVisible(False)
        self.btn_restart.setVisible(False)

        self._layout.addWidget(self.btn_start)
        self._layout.addWidget(self.btn_pause)
        self._layout.addWidget(self.btn_restart)
        self._layout.addSpacerItem(QSpacerItem(20, 1, QSizePolicy.Policy.Expanding))

        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["English", "فارسی", "中文"])
        self.lang_combo.setMinimumWidth(90)
        self.lang_combo.setMinimumHeight(34)
        self.lang_combo.currentIndexChanged.connect(self._on_lang)

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Dark", "Light"])
        self.theme_combo.setMinimumWidth(80)
        self.theme_combo.setMinimumHeight(34)
        self.theme_combo.currentIndexChanged.connect(self._on_theme)

        lbl_lang = QLabel()
        lbl_theme = QLabel()
        self._lbl_lang = lbl_lang
        self._lbl_theme = lbl_theme

        self._layout.addWidget(lbl_lang)
        self._layout.addWidget(self.lang_combo)
        self._layout.addWidget(lbl_theme)
        self._layout.addWidget(self.theme_combo)

        self.btn_start.clicked.connect(self._on_start)
        self.btn_pause.clicked.connect(self._on_pause)
        self.btn_restart.clicked.connect(self._on_restart)

        self._update_texts()
        self._apply_style()

    def _on_start(self):
        self._running = True
        self._paused = False
        self.btn_start.setVisible(False)
        self.btn_pause.setVisible(True)
        self.btn_restart.setVisible(True)
        self.start_clicked.emit()

    def _on_pause(self):
        self._paused = not self._paused
        self._update_texts()
        self.pause_clicked.emit()

    def _on_restart(self):
        self._running = True
        self._paused = False
        self._update_texts()
        self.btn_start.setVisible(False)
        self.btn_pause.setVisible(True)
        self.btn_restart.setVisible(True)
        self.restart_clicked.emit()

    def _on_lang(self, idx):
        langs = ["en", "fa", "zh"]
        self.lang = langs[idx]
        self._update_texts()
        self.lang_changed.emit(self.lang)

    def _on_theme(self, idx):
        self.theme_changed.emit("dark" if idx == 0 else "light")

    def show_start(self):
        self._running = False
        self._paused = False
        self.btn_start.setVisible(True)
        self.btn_pause.setVisible(False)
        self.btn_restart.setVisible(False)
        self._update_texts()

    def set_theme(self, theme):
        self.theme = theme
        self._apply_style()

    def set_lang(self, lang):
        self.lang = lang
        self._update_texts()

    def _update_texts(self):
        tr = TRANSLATIONS[self.lang]
        self.btn_start.setText(tr["start"])
        if self._paused:
            self.btn_pause.setText(tr["resume"])
        else:
            self.btn_pause.setText(tr["pause"])
        self.btn_restart.setText(tr["restart"])
        self._lbl_lang.setText(tr["language"] + ":")
        self._lbl_theme.setText(tr["theme"] + ":")
        self._apply_style()

    def _apply_style(self):
        t = self.theme
        btn_style = f"""
            QPushButton {{
                background-color: {t["button_bg"]};
                color: {t["button_text"]};
                border: 2px solid {t["border2"]};
                border-radius: 8px;
                font-size: 13px;
                font-weight: bold;
                padding: 4px 14px;
            }}
            QPushButton:hover {{
                background-color: {t["button_hover"]};
                border-color: {t["accent3"]};
            }}
            QPushButton:pressed {{
                background-color: {t["accent"]};
            }}
        """
        for btn in [self.btn_start, self.btn_pause, self.btn_restart]:
            btn.setStyleSheet(btn_style)

        combo_style = f"""
            QComboBox {{
                background-color: {t["panel"]};
                color: {t["text"]};
                border: 1.5px solid {t["border"]};
                border-radius: 7px;
                font-size: 12px;
                padding: 2px 8px;
            }}
            QComboBox::drop-down {{
                border: none;
            }}
            QComboBox QAbstractItemView {{
                background-color: {t["panel"]};
                color: {t["text"]};
                selection-background-color: {t["accent"]};
            }}
        """
        self.lang_combo.setStyleSheet(combo_style)
        self.theme_combo.setStyleSheet(combo_style)

        lbl_style = f"color: {t['text2']}; font-size: 12px;"
        self._lbl_lang.setStyleSheet(lbl_style)
        self._lbl_theme.setStyleSheet(lbl_style)

        self.setStyleSheet(f"background-color: {t['panel']}; border-top: 1.5px solid {t['border']};")


class TitleWidget(QWidget):
    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.lang = lang
        self.setMaximumHeight(56)
        self.setMinimumHeight(42)

    def set_theme(self, theme):
        self.theme = theme
        self.update()

    def set_lang(self, lang):
        self.lang = lang
        self.update()

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        w, h = self.width(), self.height()
        t = self.theme

        grad = QLinearGradient(0, 0, w, 0)
        grad.setColorAt(0, QColor(t["bg"]))
        grad.setColorAt(0.4, QColor(t["panel2"]))
        grad.setColorAt(1, QColor(t["bg"]))
        p.fillRect(0, 0, w, h, grad)

        fs = max(14, int(min(w, h * 4) * 0.028))
        p.setFont(QFont("Arial", fs, QFont.Weight.Bold))

        title = TRANSLATIONS[self.lang]["title"]
        text_grad = QLinearGradient(w * 0.3, 0, w * 0.7, 0)
        text_grad.setColorAt(0, QColor(t["accent"]))
        text_grad.setColorAt(0.5, QColor(t["accent2"]))
        text_grad.setColorAt(1, QColor(t["accent3"]))
        p.setPen(QPen(QColor(t["accent"]), 0))

        path = QPainterPath()
        path.addText((w - QFontMetrics(p.font()).horizontalAdvance(title)) // 2,
                      h // 2 + fs // 3, p.font(), title)
        p.fillPath(path, QBrush(text_grad))

        p.setPen(QPen(QColor(t["accent3"] + "44"), 1))
        p.drawLine(0, h - 1, w, h - 1)
        p.end()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TURBO RACE 3D")
        self.setMinimumSize(640, 480)
        self.resize(960, 660)

        self._theme_name = "dark"
        self._theme = DARK_THEME
        self._lang = "en"
        self._running = False
        self._paused = False
        self._game_state = GameState(total_laps=3, difficulty="medium")

        self._setup_ui()
        self._apply_theme()

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._game_tick)
        self._timer.setInterval(16)

        self._dt = 1 / 60

    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self._title = TitleWidget(self._theme, self._lang)
        main_layout.addWidget(self._title)

        game_area = QWidget()
        game_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        game_layout = QVBoxLayout(game_area)
        game_layout.setContentsMargins(0, 0, 0, 0)
        game_layout.setSpacing(0)
        main_layout.addWidget(game_area, 1)

        self._canvas = RaceCanvas(self._game_state, self._theme)
        self._canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        game_layout.addWidget(self._canvas, 1)

        self._hud = HUDWidget(self._game_state, self._theme, self._lang, self._canvas)
        self._hud.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        self._game_over_overlay = GameOverOverlay(self._game_state, self._theme, self._lang,
                                                   self._canvas)
        self._game_over_overlay.setVisible(False)

        self._game_over_layout = QVBoxLayout(self._game_over_overlay)
        self._game_over_layout.setContentsMargins(0, 0, 0, 0)

        self._btn_play_again = QPushButton()
        self._btn_play_again.setFixedSize(180, 44)
        self._btn_play_again.clicked.connect(self._restart_game)

        over_btn_container = QWidget(self._game_over_overlay)
        over_btn_container.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        over_btn_layout = QVBoxLayout(over_btn_container)
        over_btn_layout.addStretch()
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        btn_row.addWidget(self._btn_play_again)
        btn_row.addStretch()
        over_btn_layout.addLayout(btn_row)
        over_btn_layout.addSpacing(40)

        self._game_over_layout.addWidget(over_btn_container)

        self._control_bar = ControlBar(self._theme, self._lang)
        main_layout.addWidget(self._control_bar)

        self._control_bar.start_clicked.connect(self._start_game)
        self._control_bar.pause_clicked.connect(self._toggle_pause)
        self._control_bar.restart_clicked.connect(self._restart_game)
        self._control_bar.theme_changed.connect(self._change_theme)
        self._control_bar.lang_changed.connect(self._change_lang)

        self._canvas.installEventFilter(self)
        self._canvas_resize_timer = QTimer(self)
        self._canvas_resize_timer.setSingleShot(True)
        self._canvas_resize_timer.timeout.connect(self._reposition_overlays)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._canvas_resize_timer.start(10)

    def _reposition_overlays(self):
        w = self._canvas.width()
        h = self._canvas.height()
        self._hud.setGeometry(0, 0, w, h)
        self._game_over_overlay.setGeometry(0, 0, w, h)

    def showEvent(self, event):
        super().showEvent(event)
        QTimer.singleShot(50, self._reposition_overlays)

    def eventFilter(self, obj, event):
        from PyQt6.QtCore import QEvent
        if obj == self._canvas and event.type() == QEvent.Type.Resize:
            self._reposition_overlays()
        return super().eventFilter(obj, event)

    def _apply_theme(self):
        t = self._theme
        self.setStyleSheet(f"background-color: {t['bg']}; color: {t['text']};")
        self._update_play_again_style()

    def _update_play_again_style(self):
        t = self._theme
        self._btn_play_again.setStyleSheet(f"""
            QPushButton {{
                background-color: {t['button_bg']};
                color: {t['button_text']};
                border: 2px solid {t['border2']};
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {t['button_hover']};
            }}
        """)
        self._btn_play_again.setText(TRANSLATIONS[self._lang]["play_again"])

    def _change_theme(self, name):
        self._theme_name = name
        self._theme = DARK_THEME if name == "dark" else LIGHT_THEME
        self._canvas.set_theme(self._theme)
        self._hud.set_theme(self._theme)
        self._game_over_overlay.set_theme(self._theme)
        self._title.set_theme(self._theme)
        self._control_bar.set_theme(self._theme)
        self._apply_theme()

    def _change_lang(self, lang):
        self._lang = lang
        self._hud.set_lang(lang)
        self._game_over_overlay.set_lang(lang)
        self._title.set_lang(lang)
        self._control_bar.set_lang(lang)
        self._update_play_again_style()
        self._title.update()

    def _start_game(self):
        self._game_state.reset()
        self._running = True
        self._paused = False
        self._game_over_overlay.setVisible(False)
        self._canvas.setFocus()
        self._timer.start()

    def _toggle_pause(self):
        self._paused = not self._paused
        if self._paused:
            self._timer.stop()
        else:
            self._timer.start()
            self._canvas.setFocus()

    def _restart_game(self):
        self._game_state.reset()
        self._running = True
        self._paused = False
        self._game_over_overlay.setVisible(False)
        self._control_bar.show_start()
        self._control_bar._on_start()
        self._canvas.setFocus()
        self._timer.start()

    def _game_tick(self):
        if not self._running or self._paused:
            return
        gs = self._game_state
        dt = self._dt

        keys = gs.keys
        accel = (keys[Qt.Key.Key_Up] or keys[Qt.Key.Key_W])
        brake = (keys[Qt.Key.Key_Down] or keys[Qt.Key.Key_S])
        left = (keys[Qt.Key.Key_Left] or keys[Qt.Key.Key_A])
        right = (keys[Qt.Key.Key_Right] or keys[Qt.Key.Key_D])
        nitro_key = keys[Qt.Key.Key_Space]

        max_spd = gs.max_speed
        nitro_boost = 1.0

        if nitro_key and gs.nitro > 0 and gs.nitro_cooldown <= 0:
            gs.nitro_active = True
            gs.nitro = max(0, gs.nitro - 55 * dt)
            nitro_boost = 1.55
            if gs.nitro <= 0:
                gs.nitro_cooldown = 3.0
                gs.nitro_active = False
        else:
            gs.nitro_active = False
            if gs.nitro_cooldown > 0:
                gs.nitro_cooldown -= dt
            else:
                gs.nitro = min(100, gs.nitro + 18 * dt)

        if accel:
            gs.player_speed = min(gs.player_speed + gs.acceleration * nitro_boost,
                                   max_spd * nitro_boost)
        elif brake:
            gs.player_speed = max(0, gs.player_speed - gs.braking)
        else:
            gs.player_speed *= gs.friction
            if gs.player_speed < 0.5:
                gs.player_speed = 0

        if left:
            gs.player_x = max(-0.85, gs.player_x - 0.035 * (1 + gs.player_speed / max_spd))
        if right:
            gs.player_x = min(0.85, gs.player_x + 0.035 * (1 + gs.player_speed / max_spd))

        gs.player_pos += gs.player_speed * dt * 0.4
        gs.player_total += gs.player_speed * dt * 0.01
        track_len = self._canvas.road.track_length
        if gs.player_pos >= track_len:
            gs.player_pos -= track_len
            gs.player_lap += 1
            lap_time = gs.total_time - gs.lap_start
            gs.lap_start = gs.total_time
            if gs.best_lap is None or lap_time < gs.best_lap:
                gs.best_lap = lap_time
            gs.score += int(1000 + max(0, 60 - lap_time) * 20)
            if gs.player_lap >= gs.total_laps:
                gs.finished = True
                gs.score += max(0, int(3000 - gs.total_time * 5))
                self._running = False
                self._timer.stop()
                self._game_over_overlay.setVisible(True)
                self._game_over_overlay.update()
                self._control_bar.show_start()
                return

        gs.total_time += dt
        gs.score += gs.player_speed * dt * 0.08

        for opp in gs.opponents:
            opp.update(dt, gs.difficulty)

        self._canvas.update()
        self._hud.update()

    def keyPressEvent(self, event):
        key = event.key()
        if key in self._game_state.keys:
            self._game_state.keys[key] = True
        super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        key = event.key()
        if key in self._game_state.keys:
            self._game_state.keys[key] = False
        super().keyReleaseEvent(event)

    def closeEvent(self, event):
        self._timer.stop()
        super().closeEvent(event)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("TURBO RACE 3D")
    app.setStyle("Fusion")

    font = QFont("Arial", 11)
    app.setFont(font)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
