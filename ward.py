"""
===============================================================================
WANDERLY ELITE — LUXURY TRAVEL & TOUR MANAGEMENT SYSTEM
===============================================================================

A fully upgraded Python desktop travel-management application.

FEATURES
--------
• Premium modern Tkinter interface
• Animated welcome screen
• Luxury dashboard
• Tour package explorer
• Search, filtering and sorting
• Package details popup
• Booking system
• Live booking price calculator
• Customer validation
• SQLite database
• Booking management
• Booking search
• Booking cancellation
• Digital boarding pass
• Revenue analytics
• Category analytics
• Recent booking activity
• Customer statistics
• Upcoming-trip statistics
• Theme-style visual system
• Keyboard shortcuts
• Hover effects
• Scrollable interfaces
• Export bookings to CSV
• Database backup
• About page
• Professional status bar
• No external packages required

RUN:
    python wanderly_elite.py

===============================================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv
import os
import shutil
import random
import re
from datetime import datetime, timedelta


# =============================================================================
# APPLICATION CONFIGURATION
# =============================================================================

APP_NAME = "WANDERLY ELITE"
APP_VERSION = "3.0"
DB_NAME = "wanderly_elite.db"


# =============================================================================
# PREMIUM COLOR SYSTEM
# =============================================================================

BG = "#070B14"
BG_2 = "#0A1020"
SIDEBAR = "#0B1220"
HEADER = "#0D1628"
CARD = "#101B2E"
CARD_2 = "#13223A"
INPUT = "#15243D"

WHITE = "#FFFFFF"
TEXT = "#E8EEF8"
MUTED = "#8998AD"
SUBTLE = "#53657D"

PRIMARY = "#FF4F70"
PRIMARY_HOVER = "#FF718A"

CYAN = "#35C9FF"
BLUE = "#5B8CFF"
GREEN = "#23D18B"
GOLD = "#F4C95D"
ORANGE = "#FF9F43"
PURPLE = "#A78BFA"
RED = "#FF5364"

BORDER = "#20314B"
BORDER_GOLD = "#D9B55A"

WHITE_SMOKE = "#F5F7FA"


# =============================================================================
# CATEGORY CONFIGURATION
# =============================================================================

CATEGORY_THEMES = {
    "Adventure": {
        "icon": "🧗",
        "color": CYAN,
        "background": "#112C42"
    },
    "Beach": {
        "icon": "🏖️",
        "color": GREEN,
        "background": "#10362F"
    },
    "Heritage": {
        "icon": "🏛️",
        "color": GOLD,
        "background": "#3B2D15"
    },
    "Nature": {
        "icon": "🌿",
        "color": "#62E57D",
        "background": "#173622"
    },
    "Luxury": {
        "icon": "💎",
        "color": PURPLE,
        "background": "#282046"
    },
    "All": {
        "icon": "🌍",
        "color": CYAN,
        "background": "#1B2638"
    }
}


# =============================================================================
# TOUR PACKAGE DATA
# =============================================================================

PACKAGES = [
    {
        "id": 1,
        "name": "Manali Adventure",
        "location": "Himachal Pradesh",
        "category": "Adventure",
        "days": 5,
        "nights": 4,
        "price": 8999,
        "rating": 4.9,
        "popular": True,
        "description": (
            "Majestic snow-capped peaks, Solang Valley adventures, "
            "river rafting and luxury mountain stays."
        ),
        "highlights": [
            "Solang Valley",
            "River Rafting",
            "Snow Adventure",
            "Mountain Resort",
            "Local Sightseeing"
        ]
    },
    {
        "id": 2,
        "name": "Goa Beach Escape",
        "location": "Goa, Western Coast",
        "category": "Beach",
        "days": 4,
        "nights": 3,
        "price": 7499,
        "rating": 4.8,
        "popular": True,
        "description": (
            "Golden beaches, sunset cruises, Portuguese heritage, "
            "coastal food and vibrant nightlife."
        ),
        "highlights": [
            "Baga Beach",
            "Sunset Cruise",
            "Water Sports",
            "Old Goa",
            "Beach Resort"
        ]
    },
    {
        "id": 3,
        "name": "Rajasthan Royal Tour",
        "location": "Jaipur & Jodhpur",
        "category": "Heritage",
        "days": 6,
        "nights": 5,
        "price": 11999,
        "rating": 4.9,
        "popular": True,
        "description": (
            "Experience royal palaces, magnificent forts, desert safaris "
            "and traditional Rajasthani culture."
        ),
        "highlights": [
            "Amer Fort",
            "City Palace",
            "Mehrangarh Fort",
            "Camel Safari",
            "Royal Dinner"
        ]
    },
    {
        "id": 4,
        "name": "Kerala Paradise",
        "location": "Munnar & Alleppey",
        "category": "Nature",
        "days": 7,
        "nights": 6,
        "price": 13999,
        "rating": 4.9,
        "popular": True,
        "description": (
            "Emerald backwaters, luxury houseboats, misty tea gardens "
            "and peaceful tropical landscapes."
        ),
        "highlights": [
            "Munnar",
            "Houseboat",
            "Tea Gardens",
            "Alleppey",
            "Ayurvedic Experience"
        ]
    },
    {
        "id": 5,
        "name": "Ladakh Expedition",
        "location": "Leh & Nubra Valley",
        "category": "Adventure",
        "days": 8,
        "nights": 7,
        "price": 16999,
        "rating": 5.0,
        "popular": True,
        "description": (
            "High mountain passes, Pangong Lake, Nubra Valley, "
            "desert landscapes and spectacular Himalayan skies."
        ),
        "highlights": [
            "Pangong Lake",
            "Nubra Valley",
            "Khardung La",
            "Camel Ride",
            "Stargazing"
        ]
    },
    {
        "id": 6,
        "name": "Kashmir Dream",
        "location": "Srinagar & Gulmarg",
        "category": "Nature",
        "days": 6,
        "nights": 5,
        "price": 14999,
        "rating": 4.9,
        "popular": True,
        "description": (
            "Dal Lake shikara rides, snow-covered Gulmarg, mountain "
            "valleys and peaceful Kashmiri landscapes."
        ),
        "highlights": [
            "Dal Lake",
            "Shikara Ride",
            "Gulmarg",
            "Gondola Ride",
            "Mughal Gardens"
        ]
    },
    {
        "id": 7,
        "name": "Andaman Escape",
        "location": "Havelock & Neil Island",
        "category": "Beach",
        "days": 6,
        "nights": 5,
        "price": 19999,
        "rating": 4.8,
        "popular": False,
        "description": (
            "Crystal turquoise waters, coral reefs, scuba diving, "
            "island adventures and unforgettable sunsets."
        ),
        "highlights": [
            "Radhanagar Beach",
            "Scuba Diving",
            "Island Hopping",
            "Night Kayaking",
            "Coral Reefs"
        ]
    },
    {
        "id": 8,
        "name": "Udaipur Royal Escape",
        "location": "Udaipur, Lake City",
        "category": "Heritage",
        "days": 4,
        "nights": 3,
        "price": 9999,
        "rating": 4.7,
        "popular": False,
        "description": (
            "Lake Pichola cruises, magnificent palaces, rooftop dining "
            "and beautiful royal architecture."
        ),
        "highlights": [
            "Lake Pichola",
            "City Palace",
            "Boat Cruise",
            "Royal Dinner",
            "Vintage Walk"
        ]
    },
    {
        "id": 9,
        "name": "Dubai Luxury Escape",
        "location": "Dubai, UAE",
        "category": "Luxury",
        "days": 5,
        "nights": 4,
        "price": 45999,
        "rating": 4.9,
        "popular": False,
        "description": (
            "A premium international escape featuring skyscrapers, "
            "desert adventures and luxury shopping."
        ),
        "highlights": [
            "Burj Khalifa",
            "Desert Safari",
            "Marina Cruise",
            "Luxury Shopping",
            "Dubai Mall"
        ]
    },
    {
        "id": 10,
        "name": "Sikkim Serenity",
        "location": "Gangtok & Pelling",
        "category": "Nature",
        "days": 6,
        "nights": 5,
        "price": 12999,
        "rating": 4.8,
        "popular": False,
        "description": (
            "Peaceful monasteries, Himalayan viewpoints, mountain lakes "
            "and colorful Sikkimese culture."
        ),
        "highlights": [
            "Gangtok",
            "Pelling",
            "Tsomgo Lake",
            "Monasteries",
            "Himalayan Views"
        ]
    },
    {
        "id": 11,
        "name": "Rishikesh Adventure",
        "location": "Uttarakhand",
        "category": "Adventure",
        "days": 3,
        "nights": 2,
        "price": 5999,
        "rating": 4.7,
        "popular": False,
        "description": (
            "River rafting, camping, cliff adventures and peaceful "
            "Ganga-side experiences."
        ),
        "highlights": [
            "River Rafting",
            "Camping",
            "Bungee Jump",
            "Ganga Aarti",
            "Yoga"
        ]
    },
    {
        "id": 12,
        "name": "Mysore Heritage",
        "location": "Mysore, Karnataka",
        "category": "Heritage",
        "days": 4,
        "nights": 3,
        "price": 7999,
        "rating": 4.6,
        "popular": False,
        "description": (
            "Explore royal palaces, historical architecture, gardens "
            "and South Indian culture."
        ),
        "highlights": [
            "Mysore Palace",
            "Chamundi Hills",
            "Brindavan Gardens",
            "Local Food",
            "Heritage Walk"
        ]
    }
]


# =============================================================================
# DATABASE
# =============================================================================

def get_db():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def init_database():
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            package TEXT NOT NULL,
            category TEXT,
            travel_date TEXT NOT NULL,
            travelers INTEGER NOT NULL,
            total_price REAL NOT NULL,
            booking_date TEXT NOT NULL,
            status TEXT DEFAULT 'Confirmed'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS app_settings (
            setting TEXT PRIMARY KEY,
            value TEXT
        )
    """)

    cursor.execute("SELECT COUNT(*) AS count FROM bookings")

    if cursor.fetchone()["count"] == 0:
        sample_data = [
            (
                "Aarav Sharma",
                "+91 98765 43210",
                "aarav@example.com",
                "Manali Adventure",
                "Adventure",
                "25-10-2026",
                2,
                17998,
                "12-10-2026 14:30",
                "Confirmed"
            ),
            (
                "Priya Patel",
                "+91 91234 56789",
                "priya@example.com",
                "Goa Beach Escape",
                "Beach",
                "02-11-2026",
                4,
                29996,
                "13-10-2026 10:15",
                "Confirmed"
            ),
            (
                "Vikram Singhania",
                "+91 99887 76655",
                "vikram@example.com",
                "Rajasthan Royal Tour",
                "Heritage",
                "18-11-2026",
                2,
                23998,
                "14-10-2026 18:45",
                "Confirmed"
            )
        ]

        cursor.executemany("""
            INSERT INTO bookings
            (
                customer_name,
                phone,
                email,
                package,
                category,
                travel_date,
                travelers,
                total_price,
                booking_date,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, sample_data)

    connection.commit()
    connection.close()


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def money(value):
    return f"₹{float(value):,.0f}"


def get_package(name):
    for package in PACKAGES:
        if package["name"] == name:
            return package
    return None


def validate_email(email):
    if not email:
        return True

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return bool(re.match(pattern, email))


def validate_phone(phone):
    digits = re.sub(r"\D", "", phone)
    return len(digits) >= 10


def parse_date(value):
    return datetime.strptime(value, "%d-%m-%Y")


def days_until(value):
    try:
        return (parse_date(value).date() - datetime.now().date()).days
    except ValueError:
        return 9999


# =============================================================================
# MAIN APPLICATION
# =============================================================================

class WanderlyApp:

    def __init__(self, root):
        self.root = root

        self.root.title(
            f"{APP_NAME} — Luxury Travel & Tour Management"
        )

        self.root.geometry("1450x900")
        self.root.minsize(1100, 720)
        self.root.configure(bg=BG)

        self.sidebar_buttons = {}
        self.current_page = "dashboard"
        self.status_var = tk.StringVar(
            value="Ready • Welcome to Wanderly Elite"
        )

        self.setup_styles()
        self.build_interface()
        self.bind_shortcuts()

        self.show_splash()

    # =========================================================================
    # STYLING
    # =========================================================================

    def setup_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Treeview",
            background=CARD,
            foreground=TEXT,
            fieldbackground=CARD,
            borderwidth=0,
            rowheight=42,
            font=("Segoe UI", 9)
        )

        style.configure(
            "Treeview.Heading",
            background="#182941",
            foreground=WHITE,
            borderwidth=0,
            padding=10,
            font=("Segoe UI", 9, "bold")
        )

        style.map(
            "Treeview",
            background=[
                ("selected", PRIMARY)
            ],
            foreground=[
                ("selected", WHITE)
            ]
        )

        style.configure(
            "TCombobox",
            fieldbackground=INPUT,
            background=INPUT,
            foreground=WHITE,
            arrowcolor=WHITE
        )

    # =========================================================================
    # ROOT INTERFACE
    # =========================================================================

    def build_interface(self):

        self.header = tk.Frame(
            self.root,
            bg=HEADER,
            height=76
        )

        self.header.pack(
            fill="x",
            side="top"
        )

        self.header.pack_propagate(False)

        self.build_header()

        self.body = tk.Frame(
            self.root,
            bg=BG
        )

        self.body.pack(
            fill="both",
            expand=True
        )

        self.sidebar = tk.Frame(
            self.body,
            bg=SIDEBAR,
            width=250
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        self.build_sidebar()

        self.content = tk.Frame(
            self.body,
            bg=BG
        )

        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.build_status_bar()

    # =========================================================================
    # HEADER
    # =========================================================================

    def build_header(self):

        left = tk.Frame(
            self.header,
            bg=HEADER
        )

        left.pack(
            side="left",
            fill="y",
            padx=28
        )

        logo = tk.Label(
            left,
            text="✈",
            font=("Segoe UI Symbol", 27),
            bg=HEADER,
            fg=GOLD
        )

        logo.pack(
            side="left",
            padx=(0, 12)
        )

        brand = tk.Frame(
            left,
            bg=HEADER
        )

        brand.pack(
            side="left"
        )

        tk.Label(
            brand,
            text="WANDERLY",
            font=("Segoe UI", 19, "bold"),
            bg=HEADER,
            fg=WHITE
        ).pack(
            anchor="w"
        )

        tk.Label(
            brand,
            text="ELITE TRAVEL MANAGEMENT",
            font=("Segoe UI", 7, "bold"),
            bg=HEADER,
            fg=BORDER_GOLD
        ).pack(
            anchor="w"
        )

        right = tk.Frame(
            self.header,
            bg=HEADER
        )

        right.pack(
            side="right",
            padx=25
        )

        self.clock_label = tk.Label(
            right,
            text="",
            font=("Segoe UI", 9, "bold"),
            bg=HEADER,
            fg=MUTED
        )

        self.clock_label.pack(
            side="left",
            padx=15
        )

        tk.Button(
            right,
            text="＋ NEW BOOKING",
            command=self.open_quick_booking,
            font=("Segoe UI", 9, "bold"),
            bg=PRIMARY,
            fg=WHITE,
            activebackground=PRIMARY_HOVER,
            activeforeground=WHITE,
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=9
        ).pack(
            side="left"
        )

        self.update_clock()

    def update_clock(self):

        if not self.root.winfo_exists():
            return

        self.clock_label.config(
            text=datetime.now().strftime(
                "%A • %d %B %Y • %I:%M:%S %p"
            )
        )

        self.root.after(
            1000,
            self.update_clock
        )

    # =========================================================================
    # SIDEBAR
    # =========================================================================

    def build_sidebar(self):

        top = tk.Frame(
            self.sidebar,
            bg=SIDEBAR
        )

        top.pack(
            fill="x",
            padx=22,
            pady=(28, 15)
        )

        tk.Label(
            top,
            text="COMMAND CENTER",
            font=("Segoe UI", 8, "bold"),
            bg=SIDEBAR,
            fg=MUTED
        ).pack(
            anchor="w"
        )

        navigation = [
            ("⌂", "Dashboard", self.dashboard, "dashboard"),
            ("🌍", "Tour Packages", self.show_packages, "packages"),
            ("🎫", "Bookings", self.view_bookings, "bookings"),
            ("📊", "Analytics", self.analytics, "analytics"),
            ("❌", "Cancel Booking", self.cancel_booking, "cancel"),
            ("💾", "Data Center", self.data_center, "data"),
            ("ℹ", "About", self.about, "about")
        ]

        for icon, text, command, key in navigation:

            self.create_nav_button(
                icon,
                text,
                command,
                key
            )

        spacer = tk.Frame(
            self.sidebar,
            bg=SIDEBAR
        )

        spacer.pack(
            fill="both",
            expand=True
        )

        system_card = tk.Frame(
            self.sidebar,
            bg="#101B2E",
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=15,
            pady=13
        )

        system_card.pack(
            fill="x",
            padx=14,
            pady=10
        )

        tk.Label(
            system_card,
            text="● SYSTEM ONLINE",
            font=("Segoe UI", 8, "bold"),
            bg="#101B2E",
            fg=GREEN
        ).pack(
            anchor="w"
        )

        tk.Label(
            system_card,
            text=f"Version {APP_VERSION}",
            font=("Segoe UI", 8),
            bg="#101B2E",
            fg=MUTED
        ).pack(
            anchor="w",
            pady=(4, 0)
        )

        tk.Button(
            self.sidebar,
            text="🚪   Exit Application",
            command=self.exit_application,
            anchor="w",
            font=("Segoe UI", 9, "bold"),
            bg=SIDEBAR,
            fg=RED,
            activebackground=RED,
            activeforeground=WHITE,
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=14
        ).pack(
            fill="x",
            padx=12,
            pady=(0, 20)
        )

    def create_nav_button(
        self,
        icon,
        text,
        command,
        key
    ):

        button = tk.Button(
            self.sidebar,
            text=f"{icon}   {text}",
            command=lambda: self.navigate(
                command,
                key
            ),
            anchor="w",
            font=("Segoe UI", 10, "bold"),
            bg=SIDEBAR,
            fg=TEXT,
            activebackground="#182941",
            activeforeground=WHITE,
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=13
        )

        button.pack(
            fill="x",
            padx=12,
            pady=3
        )

        self.sidebar_buttons[key] = button

        return button

    def navigate(self, command, key):

        self.current_page = key

        self.set_active_nav(key)

        command()

    def set_active_nav(self, key):

        for name, button in self.sidebar_buttons.items():

            if name == key:
                button.config(
                    bg="#182941",
                    fg=WHITE
                )
            else:
                button.config(
                    bg=SIDEBAR,
                    fg=TEXT
                )

    # =========================================================================
    # STATUS BAR
    # =========================================================================

    def build_status_bar(self):

        self.status_bar = tk.Frame(
            self.root,
            bg="#0A111F",
            height=30
        )

        self.status_bar.pack(
            side="bottom",
            fill="x"
        )

        self.status_bar.pack_propagate(False)

        tk.Label(
            self.status_bar,
            textvariable=self.status_var,
            font=("Segoe UI", 8),
            bg="#0A111F",
            fg=MUTED,
            anchor="w"
        ).pack(
            side="left",
            padx=15
        )

        tk.Label(
            self.status_bar,
            text="SQLite • Python • Tkinter • Offline Ready",
            font=("Segoe UI", 8),
            bg="#0A111F",
            fg=SUBTLE
        ).pack(
            side="right",
            padx=15
        )

    def set_status(self, text):

        self.status_var.set(
            f"●  {text}"
        )

    # =========================================================================
    # SPLASH SCREEN
    # =========================================================================

    def show_splash(self):

        splash = tk.Toplevel(self.root)

        splash.overrideredirect(True)
        splash.configure(bg=BG)

        width = 620
        height = 380

        screen_w = splash.winfo_screenwidth()
        screen_h = splash.winfo_screenheight()

        x = (screen_w - width) // 2
        y = (screen_h - height) // 2

        splash.geometry(
            f"{width}x{height}+{x}+{y}"
        )

        canvas = tk.Canvas(
            splash,
            bg=BG,
            highlightthickness=0
        )

        canvas.pack(
            fill="both",
            expand=True
        )

        canvas.create_text(
            width // 2,
            105,
            text="✈",
            font=("Segoe UI Symbol", 60),
            fill=GOLD
        )

        canvas.create_text(
            width // 2,
            180,
            text="WANDERLY",
            font=("Segoe UI", 30, "bold"),
            fill=WHITE
        )

        canvas.create_text(
            width // 2,
            220,
            text="ELITE TRAVEL MANAGEMENT",
            font=("Segoe UI", 9, "bold"),
            fill=BORDER_GOLD
        )

        canvas.create_text(
            width // 2,
            270,
            text="Crafting extraordinary journeys...",
            font=("Segoe UI", 10),
            fill=MUTED
        )

        progress = ttk.Progressbar(
            splash,
            mode="determinate",
            maximum=100
        )

        progress.place(
            x=95,
            y=320,
            width=430,
            height=7
        )

        def animate(value=0):

            if value <= 100:
                progress["value"] = value
                splash.after(
                    14,
                    lambda: animate(value + 2)
                )
            else:
                splash.destroy()
                self.dashboard()

        splash.after(
            150,
            animate
        )

    # =========================================================================
    # CLEAR CONTENT
    # =========================================================================

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    # =========================================================================
    # SCROLLABLE FRAME
    # =========================================================================

    def create_scrollable(self, parent):

        container = tk.Frame(
            parent,
            bg=BG
        )

        canvas = tk.Canvas(
            container,
            bg=BG,
            highlightthickness=0
        )

        scrollbar = ttk.Scrollbar(
            container,
            orient="vertical",
            command=canvas.yview
        )

        frame = tk.Frame(
            canvas,
            bg=BG
        )

        frame.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        window = canvas.create_window(
            (0, 0),
            window=frame,
            anchor="nw"
        )

        canvas.bind(
            "<Configure>",
            lambda event: canvas.itemconfigure(
                window,
                width=event.width
            )
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        return container, canvas, frame

    # =========================================================================
    # DASHBOARD
    # =========================================================================

    def dashboard(self):

        self.clear_content()
        self.set_active_nav("dashboard")
        self.set_status("Dashboard loaded")

        container, canvas, page = self.create_scrollable(
            self.content
        )

        container.pack(
            fill="both",
            expand=True
        )

        # Header
        header = tk.Frame(
            page,
            bg=BG
        )

        header.pack(
            fill="x",
            padx=32,
            pady=(28, 18)
        )

        title_box = tk.Frame(
            header,
            bg=BG
        )

        title_box.pack(
            side="left"
        )

        tk.Label(
            title_box,
            text="Good day, Travel Manager 👋",
            font=("Segoe UI", 23, "bold"),
            bg=BG,
            fg=WHITE
        ).pack(
            anchor="w"
        )

        tk.Label(
            title_box,
            text="Your command center for extraordinary journeys.",
            font=("Segoe UI", 10),
            bg=BG,
            fg=MUTED
        ).pack(
            anchor="w",
            pady=(4, 0)
        )

        tk.Button(
            header,
            text="＋ Create New Reservation",
            command=self.open_quick_booking,
            font=("Segoe UI", 9, "bold"),
            bg=PRIMARY,
            fg=WHITE,
            activebackground=PRIMARY_HOVER,
            relief="flat",
            cursor="hand2",
            padx=17,
            pady=9
        ).pack(
            side="right"
        )

        # Hero
        hero = tk.Frame(
            page,
            bg="#0D1A30",
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=32,
            pady=27
        )

        hero.pack(
            fill="x",
            padx=32,
            pady=(0, 20)
        )

        tk.Label(
            hero,
            text="✦ PREMIUM JOURNEYS • CURATED EXPERIENCES • SEAMLESS BOOKINGS",
            font=("Segoe UI", 8, "bold"),
            bg="#0D1A30",
            fg=GOLD
        ).pack(
            anchor="w"
        )

        tk.Label(
            hero,
            text="Travel farther.\nFeel more. Remember forever.",
            font=("Segoe UI", 28, "bold"),
            bg="#0D1A30",
            fg=WHITE,
            justify="left"
        ).pack(
            anchor="w",
            pady=(8, 5)
        )

        tk.Label(
            hero,
            text=(
                "Manage premium destinations, reservations, customers "
                "and travel operations from one elegant workspace."
            ),
            font=("Segoe UI", 10),
            bg="#0D1A30",
            fg=MUTED
        ).pack(
            anchor="w",
            pady=(0, 18)
        )

        hero_actions = tk.Frame(
            hero,
            bg="#0D1A30"
        )

        hero_actions.pack(
            anchor="w"
        )

        self.make_button(
            hero_actions,
            "Explore Destinations →",
            self.show_packages,
            PRIMARY
        ).pack(
            side="left",
            padx=(0, 10)
        )

        self.make_button(
            hero_actions,
            "View Reservations",
            self.view_bookings,
            "#1B2B45"
        ).pack(
            side="left"
        )

        # Statistics
        stats = self.get_statistics()

        stats_row = tk.Frame(
            page,
            bg=BG
        )

        stats_row.pack(
            fill="x",
            padx=32,
            pady=(0, 20)
        )

        self.stat_card(
            stats_row,
            "🌍",
            str(len(PACKAGES)),
            "Tour Packages",
            "Curated destinations",
            CYAN
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 7)
        )

        self.stat_card(
            stats_row,
            "🎫",
            str(stats["bookings"]),
            "Confirmed Trips",
            "Active reservations",
            PRIMARY
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=7
        )

        self.stat_card(
            stats_row,
            "💰",
            money(stats["revenue"]),
            "Total Revenue",
            "Confirmed booking value",
            GREEN
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=7
        )

        self.stat_card(
            stats_row,
            "👥",
            str(stats["travelers"]),
            "Travelers",
            "Guests across bookings",
            PURPLE
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=(7, 0)
        )

        # Split area
        split = tk.Frame(
            page,
            bg=BG
        )

        split.pack(
            fill="x",
            padx=32,
            pady=(0, 25)
        )

        self.dashboard_trending(split)
        self.dashboard_activity(split)

    # =========================================================================
    # STAT CARD
    # =========================================================================

    def stat_card(
        self,
        parent,
        icon,
        value,
        title,
        subtitle,
        accent
    ):

        card = tk.Frame(
            parent,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=18,
            pady=16
        )

        top = tk.Frame(
            card,
            bg=CARD
        )

        top.pack(
            fill="x"
        )

        tk.Label(
            top,
            text=icon,
            font=("Segoe UI Emoji", 19),
            bg=CARD,
            fg=accent
        ).pack(
            side="left"
        )

        tk.Frame(
            top,
            bg=accent,
            width=4,
            height=23
        ).pack(
            side="right"
        )

        tk.Label(
            card,
            text=value,
            font=("Segoe UI", 19, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(
            anchor="w",
            pady=(8, 1)
        )

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 9, "bold"),
            bg=CARD,
            fg=TEXT
        ).pack(
            anchor="w"
        )

        tk.Label(
            card,
            text=subtitle,
            font=("Segoe UI", 7),
            bg=CARD,
            fg=MUTED
        ).pack(
            anchor="w",
            pady=(2, 0)
        )

        return card

    # =========================================================================
    # DASHBOARD TRENDING
    # =========================================================================

    def dashboard_trending(self, parent):

        card = tk.Frame(
            parent,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=22,
            pady=18
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8)
        )

        tk.Label(
            card,
            text="🔥 Trending Expeditions",
            font=("Segoe UI", 13, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(
            anchor="w"
        )

        tk.Label(
            card,
            text="Most attractive experiences this season",
            font=("Segoe UI", 8),
            bg=CARD,
            fg=MUTED
        ).pack(
            anchor="w",
            pady=(2, 12)
        )

        for package in PACKAGES[:5]:

            row = tk.Frame(
                card,
                bg="#14233A",
                padx=12,
                pady=10
            )

            row.pack(
                fill="x",
                pady=4
            )

            theme = CATEGORY_THEMES[
                package["category"]
            ]

            tk.Label(
                row,
                text=theme["icon"],
                font=("Segoe UI Emoji", 16),
                bg="#14233A"
            ).pack(
                side="left",
                padx=(0, 10)
            )

            info = tk.Frame(
                row,
                bg="#14233A"
            )

            info.pack(
                side="left",
                fill="x",
                expand=True
            )

            tk.Label(
                info,
                text=package["name"],
                font=("Segoe UI", 9, "bold"),
                bg="#14233A",
                fg=WHITE
            ).pack(
                anchor="w"
            )

            tk.Label(
                info,
                text=f"📍 {package['location']} • {package['days']} Days",
                font=("Segoe UI", 7),
                bg="#14233A",
                fg=MUTED
            ).pack(
                anchor="w"
            )

            tk.Label(
                row,
                text=money(package["price"]),
                font=("Segoe UI", 10, "bold"),
                bg="#14233A",
                fg=GREEN
            ).pack(
                side="right"
            )

    # =========================================================================
    # DASHBOARD ACTIVITY
    # =========================================================================

    def dashboard_activity(self, parent):

        card = tk.Frame(
            parent,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=22,
            pady=18
        )

        card.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(8, 0)
        )

        tk.Label(
            card,
            text="⚡ Recent Activity",
            font=("Segoe UI", 13, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(
            anchor="w"
        )

        tk.Label(
            card,
            text="Latest reservation activity",
            font=("Segoe UI", 8),
            bg=CARD,
            fg=MUTED
        ).pack(
            anchor="w",
            pady=(2, 12)
        )

        connection = get_db()

        records = connection.execute("""
            SELECT booking_id, customer_name, package,
                   total_price, booking_date
            FROM bookings
            ORDER BY booking_id DESC
            LIMIT 5
        """).fetchall()

        connection.close()

        if not records:

            tk.Label(
                card,
                text="No booking activity yet.",
                font=("Segoe UI", 9),
                bg=CARD,
                fg=MUTED
            ).pack(
                pady=20
            )

            return

        for record in records:

            row = tk.Frame(
                card,
                bg="#14233A",
                padx=12,
                pady=9
            )

            row.pack(
                fill="x",
                pady=4
            )

            tk.Label(
                row,
                text="●",
                font=("Segoe UI", 12),
                bg="#14233A",
                fg=GREEN
            ).pack(
                side="left",
                padx=(0, 10)
            )

            info = tk.Frame(
                row,
                bg="#14233A"
            )

            info.pack(
                side="left",
                fill="x",
                expand=True
            )

            tk.Label(
                info,
                text=record["customer_name"],
                font=("Segoe UI", 9, "bold"),
                bg="#14233A",
                fg=WHITE
            ).pack(
                anchor="w"
            )

            tk.Label(
                info,
                text=record["package"],
                font=("Segoe UI", 7),
                bg="#14233A",
                fg=MUTED
            ).pack(
                anchor="w"
            )

            tk.Label(
                row,
                text=money(record["total_price"]),
                font=("Segoe UI", 9, "bold"),
                bg="#14233A",
                fg=GREEN
            ).pack(
                side="right"
            )

    # =========================================================================
    # STATISTICS
    # =========================================================================

    def get_statistics(self):

        connection = get_db()

        bookings = connection.execute("""
            SELECT COUNT(*) AS count
            FROM bookings
            WHERE status = 'Confirmed'
        """).fetchone()["count"]

        revenue = connection.execute("""
            SELECT COALESCE(SUM(total_price), 0) AS total
            FROM bookings
            WHERE status = 'Confirmed'
        """).fetchone()["total"]

        travelers = connection.execute("""
            SELECT COALESCE(SUM(travelers), 0) AS total
            FROM bookings
            WHERE status = 'Confirmed'
        """).fetchone()["total"]

        customers = connection.execute("""
            SELECT COUNT(DISTINCT customer_name) AS count
            FROM bookings
        """).fetchone()["count"]

        connection.close()

        return {
            "bookings": bookings,
            "revenue": revenue,
            "travelers": travelers,
            "customers": customers
        }

    # =========================================================================
    # TOUR PACKAGES
    # =========================================================================

    def show_packages(self):

        self.clear_content()
        self.set_active_nav("packages")
        self.set_status("Exploring tour packages")

        top = tk.Frame(
            self.content,
            bg=BG
        )

        top.pack(
            fill="x",
            padx=30,
            pady=(25, 12)
        )

        tk.Label(
            top,
            text="Explore Destinations 🌍",
            font=("Segoe UI", 24, "bold"),
            bg=BG,
            fg=WHITE
        ).pack(
            side="left"
        )

        tk.Label(
            top,
            text=f"{len(PACKAGES)} premium experiences",
            font=("Segoe UI", 9),
            bg=BG,
            fg=MUTED
        ).pack(
            side="right",
            pady=8
        )

        toolbar = tk.Frame(
            self.content,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=16,
            pady=13
        )

        toolbar.pack(
            fill="x",
            padx=30,
            pady=(0, 15)
        )

        tk.Label(
            toolbar,
            text="🔎",
            font=("Segoe UI Emoji", 12),
            bg=CARD,
            fg=MUTED
        ).pack(
            side="left",
            padx=(0, 7)
        )

        search_var = tk.StringVar()

        search = tk.Entry(
            toolbar,
            textvariable=search_var,
            font=("Segoe UI", 10),
            bg=INPUT,
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat",
            width=28
        )

        search.pack(
            side="left",
            ipady=7,
            padx=(0, 18)
        )

        tk.Label(
            toolbar,
            text="CATEGORY",
            font=("Segoe UI", 8, "bold"),
            bg=CARD,
            fg=MUTED
        ).pack(
            side="left",
            padx=(0, 8)
        )

        category_var = tk.StringVar(
            value="All"
        )

        categories = [
            "All",
            "Adventure",
            "Beach",
            "Heritage",
            "Nature",
            "Luxury"
        ]

        category_buttons = {}

        container, canvas, grid = self.create_scrollable(
            self.content
        )

        container.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 20)
        )

        def render():

            for widget in grid.winfo_children():
                widget.destroy()

            query = search_var.get().lower().strip()
            category = category_var.get()

            selected = []

            for package in PACKAGES:

                text = (
                    package["name"] + " " +
                    package["location"] + " " +
                    package["category"]
                ).lower()

                if query and query not in text:
                    continue

                if (
                    category != "All"
                    and package["category"] != category
                ):
                    continue

                selected.append(package)

            if not selected:

                tk.Label(
                    grid,
                    text="🔍\n\nNo destinations found",
                    font=("Segoe UI", 14, "bold"),
                    bg=BG,
                    fg=MUTED,
                    justify="center"
                ).pack(
                    pady=80
                )

                return

            for index, package in enumerate(selected):

                row = index // 2
                column = index % 2

                card = self.package_card(
                    grid,
                    package
                )

                card.grid(
                    row=row,
                    column=column,
                    padx=8,
                    pady=8,
                    sticky="nsew"
                )

            grid.grid_columnconfigure(
                0,
                weight=1
            )

            grid.grid_columnconfigure(
                1,
                weight=1
            )

        def select_category(category):

            category_var.set(category)

            for name, button in category_buttons.items():

                if name == category:
                    button.config(
                        bg=PRIMARY,
                        fg=WHITE
                    )
                else:
                    button.config(
                        bg="#1A2A43",
                        fg=TEXT
                    )

            render()

        for category in categories:

            button = tk.Button(
                toolbar,
                text=category,
                command=lambda c=category: select_category(c),
                font=("Segoe UI", 8, "bold"),
                bg=PRIMARY if category == "All"
                else "#1A2A43",
                fg=WHITE if category == "All"
                else TEXT,
                activebackground=PRIMARY_HOVER,
                relief="flat",
                padx=11,
                pady=5,
                cursor="hand2"
            )

            button.pack(
                side="left",
                padx=2
            )

            category_buttons[category] = button

        sort_var = tk.StringVar(
            value="Featured"
        )

        tk.Label(
            toolbar,
            text="SORT",
            font=("Segoe UI", 8, "bold"),
            bg=CARD,
            fg=MUTED
        ).pack(
            side="right",
            padx=(12, 6)
        )

        sort_box = ttk.Combobox(
            toolbar,
            textvariable=sort_var,
            values=[
                "Featured",
                "Price: Low to High",
                "Price: High to Low",
                "Rating: Highest",
                "Duration: Longest"
            ],
            state="readonly",
            width=20
        )

        sort_box.pack(
            side="right"
        )

        def render_sorted():

            query = search_var.get().lower().strip()
            category = category_var.get()

            filtered = []

            for package in PACKAGES:

                text = (
                    package["name"] + " " +
                    package["location"] + " " +
                    package["category"]
                ).lower()

                if query and query not in text:
                    continue

                if (
                    category != "All"
                    and package["category"] != category
                ):
                    continue

                filtered.append(package)

            mode = sort_var.get()

            if mode == "Price: Low to High":
                filtered.sort(
                    key=lambda x: x["price"]
                )

            elif mode == "Price: High to Low":
                filtered.sort(
                    key=lambda x: x["price"],
                    reverse=True
                )

            elif mode == "Rating: Highest":
                filtered.sort(
                    key=lambda x: x["rating"],
                    reverse=True
                )

            elif mode == "Duration: Longest":
                filtered.sort(
                    key=lambda x: x["days"],
                    reverse=True
                )

            for widget in grid.winfo_children():
                widget.destroy()

            if not filtered:

                tk.Label(
                    grid,
                    text="🔍\n\nNo destinations found",
                    font=("Segoe UI", 14, "bold"),
                    bg=BG,
                    fg=MUTED
                ).pack(
                    pady=80
                )

                return

            for index, package in enumerate(filtered):

                card = self.package_card(
                    grid,
                    package
                )

                card.grid(
                    row=index // 2,
                    column=index % 2,
                    padx=8,
                    pady=8,
                    sticky="nsew"
                )

            grid.grid_columnconfigure(
                0,
                weight=1
            )

            grid.grid_columnconfigure(
                1,
                weight=1
            )

        search_var.trace_add(
            "write",
            lambda *_: render_sorted()
        )

        sort_box.bind(
            "<<ComboboxSelected>>",
            lambda event: render_sorted()
        )

        render()

    # =========================================================================
    # PACKAGE CARD
    # =========================================================================

    def package_card(
        self,
        parent,
        package
    ):

        theme = CATEGORY_THEMES[
            package["category"]
        ]

        card = tk.Frame(
            parent,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=18,
            pady=16
        )

        top = tk.Frame(
            card,
            bg=CARD
        )

        top.pack(
            fill="x"
        )

        badge = tk.Label(
            top,
            text=(
                f"{theme['icon']} "
                f"{package['category'].upper()}"
            ),
            font=("Segoe UI", 7, "bold"),
            bg=theme["background"],
            fg=theme["color"],
            padx=9,
            pady=4
        )

        badge.pack(
            side="left"
        )

        if package["popular"]:

            tk.Label(
                top,
                text="🔥 TRENDING",
                font=("Segoe UI", 7, "bold"),
                bg="#3B1D28",
                fg=PRIMARY,
                padx=8,
                pady=4
            ).pack(
                side="left",
                padx=7
            )

        tk.Label(
            top,
            text=f"⭐ {package['rating']}",
            font=("Segoe UI", 9, "bold"),
            bg=CARD,
            fg=GOLD
        ).pack(
            side="right"
        )

        tk.Label(
            card,
            text=package["name"],
            font=("Segoe UI", 15, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(
            anchor="w",
            pady=(15, 2)
        )

        tk.Label(
            card,
            text=f"📍 {package['location']}",
            font=("Segoe UI", 8),
            bg=CARD,
            fg=CYAN
        ).pack(
            anchor="w"
        )

        tk.Label(
            card,
            text=package["description"],
            font=("Segoe UI", 9),
            bg=CARD,
            fg=MUTED,
            wraplength=500,
            justify="left"
        ).pack(
            anchor="w",
            pady=(10, 13)
        )

        highlights = tk.Frame(
            card,
            bg=CARD
        )

        highlights.pack(
            fill="x",
            pady=(0, 15)
        )

        for item in package["highlights"][:4]:

            tk.Label(
                highlights,
                text=f"• {item}",
                font=("Segoe UI", 7),
                bg=CARD,
                fg=TEXT
            ).pack(
                side="left",
                padx=(0, 10)
            )

        separator = tk.Frame(
            card,
            bg=BORDER,
            height=1
        )

        separator.pack(
            fill="x",
            pady=(0, 13)
        )

        bottom = tk.Frame(
            card,
            bg=CARD
        )

        bottom.pack(
            fill="x"
        )

        info = tk.Frame(
            bottom,
            bg=CARD
        )

        info.pack(
            side="left"
        )

        tk.Label(
            info,
            text=f"{package['days']} DAYS / {package['nights']} NIGHTS",
            font=("Segoe UI", 7, "bold"),
            bg=CARD,
            fg=MUTED
        ).pack(
            anchor="w"
        )

        tk.Label(
            info,
            text=money(package["price"]),
            font=("Segoe UI", 16, "bold"),
            bg=CARD,
            fg=GREEN
        ).pack(
            anchor="w"
        )

        buttons = tk.Frame(
            bottom,
            bg=CARD
        )

        buttons.pack(
            side="right"
        )

        tk.Button(
            buttons,
            text="Details",
            command=lambda p=package: self.show_package_details(p),
            font=("Segoe UI", 8, "bold"),
            bg="#1A2A43",
            fg=WHITE,
            activebackground="#243B5D",
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=7
        ).pack(
            side="left",
            padx=(0, 7)
        )

        tk.Button(
            buttons,
            text="Book Now ✈",
            command=lambda p=package: self.open_booking_modal(p),
            font=("Segoe UI", 8, "bold"),
            bg=PRIMARY,
            fg=WHITE,
            activebackground=PRIMARY_HOVER,
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=7
        ).pack(
            side="left"
        )

        return card

    # =========================================================================
    # PACKAGE DETAILS
    # =========================================================================

    def show_package_details(self, package):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            f"{package['name']} — Wanderly"
        )

        window.geometry(
            "680x650"
        )

        window.configure(
            bg=BG
        )

        window.grab_set()

        theme = CATEGORY_THEMES[
            package["category"]
        ]

        header = tk.Frame(
            window,
            bg="#0E1A2D",
            padx=28,
            pady=25
        )

        header.pack(
            fill="x"
        )

        tk.Label(
            header,
            text=theme["icon"],
            font=("Segoe UI Emoji", 38),
            bg="#0E1A2D",
            fg=theme["color"]
        ).pack(
            anchor="w"
        )

        tk.Label(
            header,
            text=package["name"],
            font=("Segoe UI", 22, "bold"),
            bg="#0E1A2D",
            fg=WHITE
        ).pack(
            anchor="w"
        )

        tk.Label(
            header,
            text=(
                f"📍 {package['location']}   •   "
                f"⭐ {package['rating']}   •   "
                f"{package['days']} Days / "
                f"{package['nights']} Nights"
            ),
            font=("Segoe UI", 9),
            bg="#0E1A2D",
            fg=MUTED
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

        body = tk.Frame(
            window,
            bg=BG,
            padx=28,
            pady=22
        )

        body.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            body,
            text="Experience Overview",
            font=("Segoe UI", 13, "bold"),
            bg=BG,
            fg=WHITE
        ).pack(
            anchor="w"
        )

        tk.Label(
            body,
            text=package["description"],
            font=("Segoe UI", 10),
            bg=BG,
            fg=MUTED,
            wraplength=600,
            justify="left"
        ).pack(
            anchor="w",
            pady=(7, 18)
        )

        tk.Label(
            body,
            text="✨ EXPERIENCE HIGHLIGHTS",
            font=("Segoe UI", 8, "bold"),
            bg=BG,
            fg=GOLD
        ).pack(
            anchor="w"
        )

        highlights = tk.Frame(
            body,
            bg=BG
        )

        highlights.pack(
            fill="x",
            pady=10
        )

        for index, item in enumerate(
            package["highlights"]
        ):

            row = tk.Frame(
                highlights,
                bg="#13223A",
                padx=12,
                pady=9
            )

            row.grid(
                row=index // 2,
                column=index % 2,
                sticky="ew",
                padx=4,
                pady=4
            )

            tk.Label(
                row,
                text="✓",
                font=("Segoe UI", 10, "bold"),
                bg="#13223A",
                fg=GREEN
            ).pack(
                side="left",
                padx=(0, 8)
            )

            tk.Label(
                row,
                text=item,
                font=("Segoe UI", 8, "bold"),
                bg="#13223A",
                fg=TEXT
            ).pack(
                side="left"
            )

        highlights.grid_columnconfigure(
            0,
            weight=1
        )

        highlights.grid_columnconfigure(
            1,
            weight=1
        )

        price = tk.Frame(
            body,
            bg=CARD,
            padx=18,
            pady=14,
            highlightthickness=1,
            highlightbackground=BORDER
        )

        price.pack(
            fill="x",
            pady=(12, 15)
        )

        tk.Label(
            price,
            text="STARTING FROM",
            font=("Segoe UI", 7, "bold"),
            bg=CARD,
            fg=MUTED
        ).pack(
            anchor="w"
        )

        tk.Label(
            price,
            text=money(package["price"]),
            font=("Segoe UI", 20, "bold"),
            bg=CARD,
            fg=GREEN
        ).pack(
            anchor="w"
        )

        tk.Button(
            body,
            text="✦ Reserve This Journey",
            command=lambda: [
                window.destroy(),
                self.open_booking_modal(package)
            ],
            font=("Segoe UI", 10, "bold"),
            bg=PRIMARY,
            fg=WHITE,
            activebackground=PRIMARY_HOVER,
            relief="flat",
            cursor="hand2",
            pady=11
        ).pack(
            fill="x"
        )

    # =========================================================================
    # BOOKING MODAL
    # =========================================================================

    def open_quick_booking(self):

        self.show_packages()

        if PACKAGES:
            self.root.after(
                100,
                lambda: self.open_booking_modal(
                    PACKAGES[0]
                )
            )

    def open_booking_modal(self, package):

        modal = tk.Toplevel(
            self.root
        )

        modal.title(
            f"Reserve — {package['name']}"
        )

        modal.geometry(
            "650x790"
        )

        modal.minsize(
            600,
            700
        )

        modal.configure(
            bg=BG
        )

        modal.grab_set()

        header = tk.Frame(
            modal,
            bg="#0E1A2D",
            padx=28,
            pady=22
        )

        header.pack(
            fill="x"
        )

        tk.Label(
            header,
            text="✦ BESPOKE RESERVATION",
            font=("Segoe UI", 8, "bold"),
            bg="#0E1A2D",
            fg=GOLD
        ).pack(
            anchor="w"
        )

        tk.Label(
            header,
            text=package["name"],
            font=("Segoe UI", 21, "bold"),
            bg="#0E1A2D",
            fg=WHITE
        ).pack(
            anchor="w",
            pady=(4, 2)
        )

        tk.Label(
            header,
            text=(
                f"📍 {package['location']}  •  "
                f"{package['days']} Days / "
                f"{package['nights']} Nights"
            ),
            font=("Segoe UI", 9),
            bg="#0E1A2D",
            fg=MUTED
        ).pack(
            anchor="w"
        )

        body = tk.Frame(
            modal,
            bg=BG,
            padx=28,
            pady=18
        )

        body.pack(
            fill="both",
            expand=True
        )

        # Name
        self.form_label(
            body,
            "CUSTOMER FULL NAME *"
        )

        name_entry = self.form_entry(
            body
        )

        # Contact row
        contact = tk.Frame(
            body,
            bg=BG
        )

        contact.pack(
            fill="x",
            pady=(12, 0)
        )

        phone_col = tk.Frame(
            contact,
            bg=BG
        )

        phone_col.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 7)
        )

        self.form_label(
            phone_col,
            "PHONE NUMBER *"
        )

        phone_entry = self.form_entry(
            phone_col
        )

        email_col = tk.Frame(
            contact,
            bg=BG
        )

        email_col.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(7, 0)
        )

        self.form_label(
            email_col,
            "EMAIL ADDRESS"
        )

        email_entry = self.form_entry(
            email_col
        )

        # Date
        self.form_label(
            body,
            "DEPARTURE DATE *",
            pady=(15, 4)
        )

        date_entry = self.form_entry(
            body
        )

        date_entry.insert(
            0,
            (
                datetime.now()
                + timedelta(days=14)
            ).strftime("%d-%m-%Y")
        )

        quick_dates = tk.Frame(
            body,
            bg=BG
        )

        quick_dates.pack(
            anchor="w",
            pady=(5, 0)
        )

        for text, days in [
            ("+7 DAYS", 7),
            ("+14 DAYS", 14),
            ("+30 DAYS", 30),
            ("+60 DAYS", 60)
        ]:

            tk.Button(
                quick_dates,
                text=text,
                command=lambda d=days: self.set_date(
                    date_entry,
                    d
                ),
                font=("Segoe UI", 7, "bold"),
                bg="#182941",
                fg=CYAN,
                activebackground="#243B5D",
                relief="flat",
                cursor="hand2",
                padx=7,
                pady=4
            ).pack(
                side="left",
                padx=2
            )

        # Travelers
        self.form_label(
            body,
            "NUMBER OF TRAVELERS *",
            pady=(15, 4)
        )

        traveler_var = tk.IntVar(
            value=2
        )

        traveler_box = tk.Spinbox(
            body,
            from_=1,
            to=50,
            textvariable=traveler_var,
            font=("Segoe UI", 10, "bold"),
            bg=INPUT,
            fg=WHITE,
            insertbackground=WHITE,
            buttonbackground=PRIMARY,
            relief="flat"
        )

        traveler_box.pack(
            fill="x",
            ipady=7
        )

        # Price panel
        billing = tk.Frame(
            body,
            bg="#111D31",
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=18,
            pady=14
        )

        billing.pack(
            fill="x",
            pady=(18, 15)
        )

        base_label = tk.Label(
            billing,
            text="",
            font=("Segoe UI", 9),
            bg="#111D31",
            fg=MUTED
        )

        base_label.pack(
            anchor="w"
        )

        service_label = tk.Label(
            billing,
            text="Service & planning: Included",
            font=("Segoe UI", 8),
            bg="#111D31",
            fg=GREEN
        )

        service_label.pack(
            anchor="w",
            pady=(3, 0)
        )

        total_label = tk.Label(
            billing,
            text="",
            font=("Segoe UI", 19, "bold"),
            bg="#111D31",
            fg=GREEN
        )

        total_label.pack(
            anchor="w",
            pady=(8, 0)
        )

        def update_total(*_):

            try:
                travelers = max(
                    1,
                    int(
                        traveler_var.get()
                    )
                )
            except ValueError:
                travelers = 1

            total = (
                package["price"]
                * travelers
            )

            base_label.config(
                text=(
                    f"Base Package Rate: "
                    f"{money(package['price'])} × "
                    f"{travelers} Traveler(s)"
                )
            )

            total_label.config(
                text=f"GRAND TOTAL  {money(total)}"
            )

        traveler_var.trace_add(
            "write",
            update_total
        )

        update_total()

        # Submit
        def submit():

            name = name_entry.get().strip()
            phone = phone_entry.get().strip()
            email = email_entry.get().strip()
            date = date_entry.get().strip()

            try:
                travelers = int(
                    traveler_var.get()
                )
            except ValueError:
                travelers = 0

            if not name:
                messagebox.showwarning(
                    "Missing Name",
                    "Please enter the customer's full name.",
                    parent=modal
                )
                name_entry.focus()
                return

            if not validate_phone(phone):
                messagebox.showwarning(
                    "Invalid Phone",
                    "Please enter a valid phone number.",
                    parent=modal
                )
                phone_entry.focus()
                return

            if not validate_email(email):
                messagebox.showwarning(
                    "Invalid Email",
                    "Please enter a valid email address.",
                    parent=modal
                )
                email_entry.focus()
                return

            if travelers < 1:
                messagebox.showwarning(
                    "Invalid Travelers",
                    "Number of travelers must be at least 1.",
                    parent=modal
                )
                return

            try:
                travel_date = parse_date(
                    date
                )
            except ValueError:
                messagebox.showwarning(
                    "Invalid Date",
                    "Use date format DD-MM-YYYY.",
                    parent=modal
                )
                date_entry.focus()
                return

            if travel_date.date() <= datetime.now().date():
                messagebox.showwarning(
                    "Invalid Travel Date",
                    "Travel date must be in the future.",
                    parent=modal
                )
                return

            total = (
                package["price"]
                * travelers
            )

            booking_date = datetime.now().strftime(
                "%d-%m-%Y %H:%M"
            )

            connection = get_db()

            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO bookings
                (
                    customer_name,
                    phone,
                    email,
                    package,
                    category,
                    travel_date,
                    travelers,
                    total_price,
                    booking_date,
                    status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                name,
                phone,
                email,
                package["name"],
                package["category"],
                date,
                travelers,
                total,
                booking_date,
                "Confirmed"
            ))

            connection.commit()

            booking_id = cursor.lastrowid

            connection.close()

            modal.destroy()

            self.set_status(
                f"Booking #{booking_id:05d} created successfully"
            )

            self.show_ticket(
                booking_id,
                name,
                phone,
                email,
                package,
                date,
                travelers,
                total,
                booking_date
            )

        tk.Button(
            body,
            text="✦ CONFIRM RESERVATION & ISSUE TICKET",
            command=submit,
            font=("Segoe UI", 10, "bold"),
            bg=PRIMARY,
            fg=WHITE,
            activebackground=PRIMARY_HOVER,
            relief="flat",
            cursor="hand2",
            pady=12
        ).pack(
            fill="x"
        )

        tk.Label(
            body,
            text="🔒 Your reservation information is stored locally in SQLite.",
            font=("Segoe UI", 7),
            bg=BG,
            fg=SUBTLE
        ).pack(
            pady=(10, 0)
        )

        name_entry.focus()

    # =========================================================================
    # FORM HELPERS
    # =========================================================================

    def form_label(
        self,
        parent,
        text,
        pady=(0, 4)
    ):

        tk.Label(
            parent,
            text=text,
            font=("Segoe UI", 8, "bold"),
            bg=parent.cget("bg"),
            fg=TEXT
        ).pack(
            anchor="w",
            pady=pady
        )

    def form_entry(self, parent):

        entry = tk.Entry(
            parent,
            font=("Segoe UI", 10),
            bg=INPUT,
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat"
        )

        entry.pack(
            fill="x",
            ipady=8
        )

        return entry

    def set_date(
        self,
        entry,
        days
    ):

        entry.delete(
            0,
            tk.END
        )

        entry.insert(
            0,
            (
                datetime.now()
                + timedelta(days=days)
            ).strftime("%d-%m-%Y")
        )

    # =========================================================================
    # DIGITAL TICKET
    # =========================================================================

    def show_ticket(
        self,
        booking_id,
        name,
        phone,
        email,
        package,
        date,
        travelers,
        total,
        timestamp
    ):

        ticket = tk.Toplevel(
            self.root
        )

        ticket.title(
            f"Digital Boarding Pass #{booking_id:05d}"
        )

        ticket.geometry(
            "620x720"
        )

        ticket.configure(
            bg=BG
        )

        ticket.grab_set()

        outer = tk.Frame(
            ticket,
            bg="#0C1729",
            highlightthickness=1,
            highlightbackground=GOLD,
            padx=28,
            pady=25
        )

        outer.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        tk.Label(
            outer,
            text="✈ WANDERLY ELITE",
            font=("Segoe UI", 16, "bold"),
            bg="#0C1729",
            fg=GOLD
        ).pack()

        tk.Label(
            outer,
            text="DIGITAL EXPEDITION PASS",
            font=("Segoe UI", 8, "bold"),
            bg="#0C1729",
            fg=MUTED
        ).pack(
            pady=(3, 15)
        )

        tk.Frame(
            outer,
            bg=BORDER,
            height=1
        ).pack(
            fill="x"
        )

        def ticket_row(
            label,
            value,
            color=WHITE
        ):

            row = tk.Frame(
                outer,
                bg="#0C1729"
            )

            row.pack(
                fill="x",
                pady=6
            )

            tk.Label(
                row,
                text=label,
                font=("Segoe UI", 8),
                bg="#0C1729",
                fg=MUTED
            ).pack(
                side="left"
            )

            tk.Label(
                row,
                text=str(value),
                font=("Segoe UI", 9, "bold"),
                bg="#0C1729",
                fg=color
            ).pack(
                side="right"
            )

        ticket_row(
            "BOOKING REFERENCE",
            f"#{booking_id:05d}",
            CYAN
        )

        ticket_row(
            "TRAVELER",
            name
        )

        ticket_row(
            "PHONE",
            phone
        )

        if email:
            ticket_row(
                "EMAIL",
                email
            )

        ticket_row(
            "DESTINATION",
            package["name"],
            GOLD
        )

        ticket_row(
            "LOCATION",
            package["location"],
            CYAN
        )

        ticket_row(
            "DEPARTURE",
            date,
            PRIMARY
        )

        ticket_row(
            "TRAVELERS",
            f"{travelers} Person(s)"
        )

        ticket_row(
            "DURATION",
            f"{package['days']} Days / {package['nights']} Nights"
        )

        tk.Frame(
            outer,
            bg=BORDER,
            height=1
        ).pack(
            fill="x",
            pady=12
        )

        ticket_row(
            "TOTAL PAID",
            money(total),
            GREEN
        )

        ticket_row(
            "STATUS",
            "CONFIRMED ✓",
            GREEN
        )

        ticket_row(
            "ISSUED",
            timestamp,
            MUTED
        )

        qr_box = tk.Frame(
            outer,
            bg="#16233B",
            padx=15,
            pady=12
        )

        qr_box.pack(
            fill="x",
            pady=(15, 12)
        )

        tk.Label(
            qr_box,
            text="▦  DIGITAL VERIFICATION",
            font=("Consolas", 10, "bold"),
            bg="#16233B",
            fg=CYAN
        ).pack()

        tk.Label(
            qr_box,
            text=f"WL-{booking_id:05d}-{random.randint(1000, 9999)}",
            font=("Consolas", 11, "bold"),
            bg="#16233B",
            fg=WHITE
        ).pack(
            pady=(5, 0)
        )

        tk.Button(
            outer,
            text="Close Boarding Pass",
            command=ticket.destroy,
            font=("Segoe UI", 9, "bold"),
            bg="#1A2A43",
            fg=WHITE,
            activebackground="#243B5D",
            relief="flat",
            cursor="hand2",
            pady=9
        ).pack(
            fill="x"
        )

    # =========================================================================
    # BOOKINGS
    # =========================================================================

    def view_bookings(self):

        self.clear_content()
        self.set_active_nav("bookings")
        self.set_status("Viewing all reservations")

        top = tk.Frame(
            self.content,
            bg=BG
        )

        top.pack(
            fill="x",
            padx=30,
            pady=(25, 12)
        )

        tk.Label(
            top,
            text="Reservations Center 🎫",
            font=("Segoe UI", 24, "bold"),
            bg=BG,
            fg=WHITE
        ).pack(
            side="left"
        )

        tk.Button(
            top,
            text="＋ New Booking",
            command=self.open_quick_booking,
            font=("Segoe UI", 9, "bold"),
            bg=PRIMARY,
            fg=WHITE,
            activebackground=PRIMARY_HOVER,
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        ).pack(
            side="right"
        )

        toolbar = tk.Frame(
            self.content,
            bg=CARD,
            padx=16,
            pady=12
        )

        toolbar.pack(
            fill="x",
            padx=30,
            pady=(0, 12)
        )

        tk.Label(
            toolbar,
            text="SEARCH",
            font=("Segoe UI", 8, "bold"),
            bg=CARD,
            fg=MUTED
        ).pack(
            side="left",
            padx=(0, 7)
        )

        search_var = tk.StringVar()

        search = tk.Entry(
            toolbar,
            textvariable=search_var,
            font=("Segoe UI", 9),
            bg=INPUT,
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat",
            width=30
        )

        search.pack(
            side="left",
            ipady=7
        )

        tk.Label(
            toolbar,
            text="Search by customer, phone, package or ID",
            font=("Segoe UI", 7),
            bg=CARD,
            fg=SUBTLE
        ).pack(
            side="left",
            padx=10
        )

        table_card = tk.Frame(
            self.content,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER
        )

        table_card.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 12)
        )

        columns = (
            "ID",
            "Customer",
            "Phone",
            "Package",
            "Date",
            "Guests",
            "Amount",
            "Status"
        )

        tree = ttk.Treeview(
            table_card,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        widths = {
            "ID": 65,
            "Customer": 150,
            "Phone": 125,
            "Package": 180,
            "Date": 105,
            "Guests": 70,
            "Amount": 115,
            "Status": 100
        }

        for column in columns:

            tree.heading(
                column,
                text=column
            )

            tree.column(
                column,
                width=widths[column],
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            table_card,
            orient="vertical",
            command=tree.yview
        )

        tree.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        tree.pack(
            fill="both",
            expand=True,
            padx=2,
            pady=2
        )

        def load():

            for item in tree.get_children():
                tree.delete(item)

            query = search_var.get().lower().strip()

            connection = get_db()

            records = connection.execute("""
                SELECT
                    booking_id,
                    customer_name,
                    phone,
                    package,
                    travel_date,
                    travelers,
                    total_price,
                    status
                FROM bookings
                ORDER BY booking_id DESC
            """).fetchall()

            connection.close()

            for record in records:

                searchable = (
                    f"{record['booking_id']} "
                    f"{record['customer_name']} "
                    f"{record['phone']} "
                    f"{record['package']}"
                ).lower()

                if query and query not in searchable:
                    continue

                tree.insert(
                    "",
                    "end",
                    values=(
                        f"#{record['booking_id']:05d}",
                        record["customer_name"],
                        record["phone"],
                        record["package"],
                        record["travel_date"],
                        record["travelers"],
                        money(record["total_price"]),
                        record["status"]
                    )
                )

        search_var.trace_add(
            "write",
            lambda *_: load()
        )

        load()

        actions = tk.Frame(
            self.content,
            bg=BG
        )

        actions.pack(
            fill="x",
            padx=30,
            pady=(0, 20)
        )

        tk.Button(
            actions,
            text="👁 View Ticket",
            command=lambda: self.view_selected_ticket(tree),
            font=("Segoe UI", 9, "bold"),
            bg="#1B2B45",
            fg=WHITE,
            activebackground="#243B5D",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=9
        ).pack(
            side="left",
            padx=(0, 8)
        )

        tk.Button(
            actions,
            text="❌ Cancel Selected",
            command=lambda: self.cancel_from_tree(
                tree,
                load
            ),
            font=("Segoe UI", 9, "bold"),
            bg=RED,
            fg=WHITE,
            activebackground="#FF6D7A",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=9
        ).pack(
            side="left"
        )

        tk.Button(
            actions,
            text="↻ Refresh",
            command=load,
            font=("Segoe UI", 9, "bold"),
            bg="#1B2B45",
            fg=WHITE,
            activebackground="#243B5D",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=9
        ).pack(
            side="right"
        )

    # =========================================================================
    # VIEW SELECTED TICKET
    # =========================================================================

    def view_selected_ticket(self, tree):

        selection = tree.selection()

        if not selection:

            messagebox.showinfo(
                "Select Reservation",
                "Please select a booking first."
            )

            return

        values = tree.item(
            selection[0]
        )["values"]

        booking_id = int(
            str(values[0]).replace(
                "#",
                ""
            )
        )

        connection = get_db()

        record = connection.execute("""
            SELECT *
            FROM bookings
            WHERE booking_id = ?
        """, (booking_id,)).fetchone()

        connection.close()

        if not record:
            return

        package = get_package(
            record["package"]
        )

        if not package:
            messagebox.showerror(
                "Error",
                "Package information could not be found."
            )
            return

        self.show_ticket(
            record["booking_id"],
            record["customer_name"],
            record["phone"],
            record["email"],
            package,
            record["travel_date"],
            record["travelers"],
            record["total_price"],
            record["booking_date"]
        )

    # =========================================================================
    # CANCEL FROM TREE
    # =========================================================================

    def cancel_from_tree(
        self,
        tree,
        refresh
    ):

        selection = tree.selection()

        if not selection:

            messagebox.showinfo(
                "Select Reservation",
                "Please select a booking to cancel."
            )

            return

        values = tree.item(
            selection[0]
        )["values"]

        booking_id = int(
            str(values[0]).replace(
                "#",
                ""
            )
        )

        customer = values[1]

        if not messagebox.askyesno(
            "Confirm Cancellation",
            (
                f"Cancel reservation #{booking_id:05d}\n\n"
                f"Customer: {customer}\n\n"
                "This action cannot be undone."
            )
        ):
            return

        connection = get_db()

        connection.execute("""
            DELETE FROM bookings
            WHERE booking_id = ?
        """, (booking_id,))

        connection.commit()
        connection.close()

        refresh()

        self.set_status(
            f"Reservation #{booking_id:05d} cancelled"
        )

        messagebox.showinfo(
            "Reservation Cancelled",
            f"Booking #{booking_id:05d} has been cancelled."
        )

    # =========================================================================
    # ANALYTICS
    # =========================================================================

    def analytics(self):

        self.clear_content()
        self.set_active_nav("analytics")
        self.set_status("Analytics dashboard loaded")

        container, canvas, page = self.create_scrollable(
            self.content
        )

        container.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            page,
            text="Travel Intelligence & Analytics 📊",
            font=("Segoe UI", 24, "bold"),
            bg=BG,
            fg=WHITE
        ).pack(
            anchor="w",
            padx=30,
            pady=(25, 5)
        )

        tk.Label(
            page,
            text="Understand bookings, revenue, destinations and customer activity.",
            font=("Segoe UI", 9),
            bg=BG,
            fg=MUTED
        ).pack(
            anchor="w",
            padx=30,
            pady=(0, 18)
        )

        stats = self.get_statistics()

        row = tk.Frame(
            page,
            bg=BG
        )

        row.pack(
            fill="x",
            padx=30,
            pady=(0, 18)
        )

        self.stat_card(
            row,
            "🎫",
            stats["bookings"],
            "Reservations",
            "Confirmed bookings",
            PRIMARY
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 7)
        )

        self.stat_card(
            row,
            "💰",
            money(stats["revenue"]),
            "Revenue",
            "Gross confirmed value",
            GREEN
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=7
        )

        self.stat_card(
            row,
            "👥",
            stats["travelers"],
            "Travelers",
            "Total guests",
            CYAN
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=7
        )

        self.stat_card(
            row,
            "⭐",
            "4.9",
            "Experience Score",
            "Average platform rating",
            GOLD
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=(7, 0)
        )

        split = tk.Frame(
            page,
            bg=BG
        )

        split.pack(
            fill="x",
            padx=30
        )

        self.category_chart(
            split
        )

        self.revenue_panel(
            split
        )

        self.analytics_package_ranking(
            page
        )

    # =========================================================================
    # CATEGORY CHART
    # =========================================================================

    def category_chart(self, parent):

        card = tk.Frame(
            parent,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=22,
            pady=20
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8)
        )

        tk.Label(
            card,
            text="Package Portfolio",
            font=("Segoe UI", 13, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(
            anchor="w"
        )

        tk.Label(
            card,
            text="Distribution across travel styles",
            font=("Segoe UI", 8),
            bg=CARD,
            fg=MUTED
        ).pack(
            anchor="w",
            pady=(2, 15)
        )

        categories = {}

        for package in PACKAGES:
            categories[
                package["category"]
            ] = categories.get(
                package["category"],
                0
            ) + 1

        total = len(PACKAGES)

        for category, count in categories.items():

            theme = CATEGORY_THEMES[
                category
            ]

            row = tk.Frame(
                card,
                bg=CARD
            )

            row.pack(
                fill="x",
                pady=6
            )

            top = tk.Frame(
                row,
                bg=CARD
            )

            top.pack(
                fill="x"
            )

            tk.Label(
                top,
                text=(
                    f"{theme['icon']} "
                    f"{category}"
                ),
                font=("Segoe UI", 8, "bold"),
                bg=CARD,
                fg=TEXT
            ).pack(
                side="left"
            )

            percentage = (
                count / total
            ) * 100

            tk.Label(
                top,
                text=f"{count} packages • {percentage:.0f}%",
                font=("Segoe UI", 7),
                bg=CARD,
                fg=MUTED
            ).pack(
                side="right"
            )

            bar = tk.Canvas(
                row,
                height=9,
                bg="#182941",
                highlightthickness=0
            )

            bar.pack(
                fill="x",
                pady=(4, 0)
            )

            bar.update_idletasks()

            width = max(
                10,
                bar.winfo_width()
                * percentage
                / 100
            )

            bar.create_rectangle(
                0,
                0,
                width,
                9,
                fill=theme["color"],
                width=0
            )

    # =========================================================================
    # REVENUE PANEL
    # =========================================================================

    def revenue_panel(self, parent):

        card = tk.Frame(
            parent,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=22,
            pady=20
        )

        card.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(8, 0)
        )

        tk.Label(
            card,
            text="Revenue Snapshot",
            font=("Segoe UI", 13, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(
            anchor="w"
        )

        tk.Label(
            card,
            text="Financial performance from confirmed reservations",
            font=("Segoe UI", 8),
            bg=CARD,
            fg=MUTED
        ).pack(
            anchor="w",
            pady=(2, 16)
        )

        connection = get_db()

        records = connection.execute("""
            SELECT
                category,
                SUM(total_price) AS revenue
            FROM bookings
            WHERE status = 'Confirmed'
            GROUP BY category
            ORDER BY revenue DESC
        """).fetchall()

        connection.close()

        if not records:

            tk.Label(
                card,
                text="No revenue data available.",
                font=("Segoe UI", 9),
                bg=CARD,
                fg=MUTED
            ).pack(
                pady=30
            )

            return

        max_value = max(
            float(r["revenue"])
            for r in records
        )

        for record in records:

            category = record["category"]
            value = float(
                record["revenue"]
            )

            theme = CATEGORY_THEMES.get(
                category,
                CATEGORY_THEMES["All"]
            )

            row = tk.Frame(
                card,
                bg=CARD
            )

            row.pack(
                fill="x",
                pady=5
            )

            top = tk.Frame(
                row,
                bg=CARD
            )

            top.pack(
                fill="x"
            )

            tk.Label(
                top,
                text=category,
                font=("Segoe UI", 8, "bold"),
                bg=CARD,
                fg=TEXT
            ).pack(
                side="left"
            )

            tk.Label(
                top,
                text=money(value),
                font=("Segoe UI", 8, "bold"),
                bg=CARD,
                fg=GREEN
            ).pack(
                side="right"
            )

            progress = tk.Canvas(
                row,
                height=8,
                bg="#182941",
                highlightthickness=0
            )

            progress.pack(
                fill="x",
                pady=(4, 0)
            )

            progress.create_rectangle(
                0,
                0,
                330 * value / max_value,
                8,
                fill=theme["color"],
                width=0
            )

    # =========================================================================
    # PACKAGE RANKING
    # =========================================================================

    def analytics_package_ranking(self, page):

        card = tk.Frame(
            page,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=22,
            pady=20
        )

        card.pack(
            fill="x",
            padx=30,
            pady=18
        )

        tk.Label(
            card,
            text="🏆 Package Performance",
            font=("Segoe UI", 13, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(
            anchor="w"
        )

        connection = get_db()

        records = connection.execute("""
            SELECT
                package,
                COUNT(*) AS bookings,
                COALESCE(SUM(total_price), 0) AS revenue
            FROM bookings
            GROUP BY package
            ORDER BY bookings DESC, revenue DESC
        """).fetchall()

        connection.close()

        if not records:

            tk.Label(
                card,
                text="No booking performance data available.",
                font=("Segoe UI", 9),
                bg=CARD,
                fg=MUTED
            ).pack(
                pady=20
            )

            return

        for index, record in enumerate(records):

            row = tk.Frame(
                card,
                bg="#14233A",
                padx=14,
                pady=10
            )

            row.pack(
                fill="x",
                pady=3
            )

            tk.Label(
                row,
                text=f"#{index + 1}",
                font=("Segoe UI", 10, "bold"),
                bg="#14233A",
                fg=GOLD
            ).pack(
                side="left",
                padx=(0, 15)
            )

            tk.Label(
                row,
                text=record["package"],
                font=("Segoe UI", 9, "bold"),
                bg="#14233A",
                fg=WHITE
            ).pack(
                side="left"
            )

            tk.Label(
                row,
                text=f"{record['bookings']} booking(s)",
                font=("Segoe UI", 8),
                bg="#14233A",
                fg=MUTED
            ).pack(
                side="right",
                padx=20
            )

            tk.Label(
                row,
                text=money(record["revenue"]),
                font=("Segoe UI", 9, "bold"),
                bg="#14233A",
                fg=GREEN
            ).pack(
                side="right"
            )

    # =========================================================================
    # CANCEL BOOKING PAGE
    # =========================================================================

    def cancel_booking(self):

        self.clear_content()
        self.set_active_nav("cancel")
        self.set_status("Cancellation center")

        tk.Label(
            self.content,
            text="Cancellation Center ❌",
            font=("Segoe UI", 24, "bold"),
            bg=BG,
            fg=WHITE
        ).pack(
            anchor="w",
            padx=35,
            pady=(30, 5)
        )

        tk.Label(
            self.content,
            text="Search a reservation, review its details and confirm cancellation.",
            font=("Segoe UI", 9),
            bg=BG,
            fg=MUTED
        ).pack(
            anchor="w",
            padx=35,
            pady=(0, 20)
        )

        card = tk.Frame(
            self.content,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=30,
            pady=28
        )

        card.pack(
            fill="x",
            padx=35
        )

        tk.Label(
            card,
            text="BOOKING REFERENCE",
            font=("Segoe UI", 8, "bold"),
            bg=CARD,
            fg=MUTED
        ).pack(
            anchor="w"
        )

        input_row = tk.Frame(
            card,
            bg=CARD
        )

        input_row.pack(
            fill="x",
            pady=(7, 0)
        )

        booking_entry = tk.Entry(
            input_row,
            font=("Segoe UI", 11),
            bg=INPUT,
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat",
            width=30
        )

        booking_entry.pack(
            side="left",
            ipady=8
        )

        preview = tk.Frame(
            card,
            bg="#131F33",
            padx=20,
            pady=18
        )

        def search():

            value = booking_entry.get().strip().replace(
                "#",
                ""
            )

            if not value.isdigit():

                messagebox.showwarning(
                    "Invalid Reference",
                    "Enter a valid numeric booking ID."
                )

                return

            connection = get_db()

            record = connection.execute("""
                SELECT *
                FROM bookings
                WHERE booking_id = ?
            """, (int(value),)).fetchone()

            connection.close()

            for widget in preview.winfo_children():
                widget.destroy()

            if not record:

                messagebox.showerror(
                    "Not Found",
                    f"Booking #{int(value):05d} was not found."
                )

                preview.pack_forget()

                return

            preview.pack(
                fill="x",
                pady=(20, 0)
            )

            tk.Label(
                preview,
                text=(
                    f"✓ Reservation Found — "
                    f"#{record['booking_id']:05d}"
                ),
                font=("Segoe UI", 12, "bold"),
                bg="#131F33",
                fg=CYAN
            ).pack(
                anchor="w"
            )

            tk.Label(
                preview,
                text=(
                    f"Customer: {record['customer_name']}\n"
                    f"Phone: {record['phone']}\n"
                    f"Package: {record['package']}\n"
                    f"Travel Date: {record['travel_date']}\n"
                    f"Travelers: {record['travelers']}\n"
                    f"Total Paid: {money(record['total_price'])}"
                ),
                font=("Segoe UI", 9),
                bg="#131F33",
                fg=TEXT,
                justify="left"
            ).pack(
                anchor="w",
                pady=(10, 15)
            )

            def execute():

                confirmed = messagebox.askyesno(
                    "Permanent Cancellation",
                    (
                        f"Cancel booking #{record['booking_id']:05d}?\n\n"
                        "This reservation will be permanently removed "
                        "from the local database."
                    )
                )

                if not confirmed:
                    return

                connection = get_db()

                connection.execute("""
                    DELETE FROM bookings
                    WHERE booking_id = ?
                """, (
                    record["booking_id"],
                ))

                connection.commit()
                connection.close()

                preview.pack_forget()

                booking_entry.delete(
                    0,
                    tk.END
                )

                self.set_status(
                    f"Booking #{record['booking_id']:05d} cancelled"
                )

                messagebox.showinfo(
                    "Cancelled",
                    "Reservation cancelled successfully."
                )

            tk.Button(
                preview,
                text="❌ Confirm Permanent Cancellation",
                command=execute,
                font=("Segoe UI", 9, "bold"),
                bg=RED,
                fg=WHITE,
                activebackground="#FF7180",
                relief="flat",
                cursor="hand2",
                padx=15,
                pady=9
            ).pack(
                anchor="w"
            )

        tk.Button(
            input_row,
            text="SEARCH BOOKING 🔍",
            command=search,
            font=("Segoe UI", 9, "bold"),
            bg=PRIMARY,
            fg=WHITE,
            activebackground=PRIMARY_HOVER,
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=9
        ).pack(
            side="left",
            padx=10
        )

        booking_entry.focus()

    # =========================================================================
    # DATA CENTER
    # =========================================================================

    def data_center(self):

        self.clear_content()
        self.set_active_nav("data")
        self.set_status("Data center loaded")

        tk.Label(
            self.content,
            text="Data Center 💾",
            font=("Segoe UI", 24, "bold"),
            bg=BG,
            fg=WHITE
        ).pack(
            anchor="w",
            padx=35,
            pady=(30, 5)
        )

        tk.Label(
            self.content,
            text="Manage local database records, backups and CSV exports.",
            font=("Segoe UI", 9),
            bg=BG,
            fg=MUTED
        ).pack(
            anchor="w",
            padx=35,
            pady=(0, 20)
        )

        cards = tk.Frame(
            self.content,
            bg=BG
        )

        cards.pack(
            fill="x",
            padx=35
        )

        self.data_action_card(
            cards,
            "📤",
            "Export Bookings",
            "Save all reservation records to a CSV file.",
            "Export CSV",
            self.export_csv,
            CYAN
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8)
        )

        self.data_action_card(
            cards,
            "🛡",
            "Database Backup",
            "Create a safe copy of your Wanderly database.",
            "Create Backup",
            self.backup_database,
            GREEN
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=8
        )

        self.data_action_card(
            cards,
            "📊",
            "Refresh Statistics",
            "Recalculate dashboard and booking statistics.",
            "Refresh",
            self.refresh_current_page,
            GOLD
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=(8, 0)
        )

        info = tk.Frame(
            self.content,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=25,
            pady=20
        )

        info.pack(
            fill="x",
            padx=35,
            pady=20
        )

        tk.Label(
            info,
            text="DATABASE INFORMATION",
            font=("Segoe UI", 8, "bold"),
            bg=CARD,
            fg=GOLD
        ).pack(
            anchor="w"
        )

        size = 0

        if os.path.exists(DB_NAME):
            size = os.path.getsize(
                DB_NAME
            ) / 1024

        stats = self.get_statistics()

        information = (
            f"Database file: {os.path.abspath(DB_NAME)}\n"
            f"Database size: {size:.1f} KB\n"
            f"Confirmed reservations: {stats['bookings']}\n"
            f"Registered travelers: {stats['travelers']}\n"
            f"Current revenue: {money(stats['revenue'])}\n"
            f"Tour packages: {len(PACKAGES)}"
        )

        tk.Label(
            info,
            text=information,
            font=("Consolas", 9),
            bg=CARD,
            fg=TEXT,
            justify="left"
        ).pack(
            anchor="w",
            pady=(10, 0)
        )

    # =========================================================================
    # DATA ACTION CARD
    # =========================================================================

    def data_action_card(
        self,
        parent,
        icon,
        title,
        description,
        button_text,
        command,
        accent
    ):

        card = tk.Frame(
            parent,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=20,
            pady=20
        )

        tk.Label(
            card,
            text=icon,
            font=("Segoe UI Emoji", 27),
            bg=CARD,
            fg=accent
        ).pack(
            anchor="w"
        )

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 12, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(
            anchor="w",
            pady=(8, 3)
        )

        tk.Label(
            card,
            text=description,
            font=("Segoe UI", 8),
            bg=CARD,
            fg=MUTED,
            wraplength=260,
            justify="left"
        ).pack(
            anchor="w",
            pady=(0, 16)
        )

        tk.Button(
            card,
            text=button_text,
            command=command,
            font=("Segoe UI", 8, "bold"),
            bg="#1A2A43",
            fg=WHITE,
            activebackground="#243B5D",
            relief="flat",
            cursor="hand2",
            padx=13,
            pady=8
        ).pack(
            anchor="w"
        )

        return card

    # =========================================================================
    # CSV EXPORT
    # =========================================================================

    def export_csv(self):

        connection = get_db()

        records = connection.execute("""
            SELECT *
            FROM bookings
            ORDER BY booking_id DESC
        """).fetchall()

        connection.close()

        if not records:

            messagebox.showinfo(
                "No Data",
                "There are no bookings to export."
            )

            return

        filename = filedialog.asksaveasfilename(
            title="Export Wanderly Bookings",
            defaultextension=".csv",
            filetypes=[
                ("CSV files", "*.csv"),
                ("All files", "*.*")
            ],
            initialfile=(
                "wanderly_bookings_"
                + datetime.now().strftime(
                    "%Y%m%d_%H%M"
                )
                + ".csv"
            )
        )

        if not filename:
            return

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(
                file
            )

            writer.writerow(
                records[0].keys()
            )

            for record in records:
                writer.writerow(
                    tuple(record)
                )

        self.set_status(
            "Booking data exported successfully"
        )

        messagebox.showinfo(
            "Export Complete",
            (
                f"{len(records)} booking(s) "
                "exported successfully."
            )
        )

    # =========================================================================
    # DATABASE BACKUP
    # =========================================================================

    def backup_database(self):

        if not os.path.exists(
            DB_NAME
        ):

            messagebox.showerror(
                "Database Missing",
                "The database file could not be found."
            )

            return

        filename = filedialog.asksaveasfilename(
            title="Backup Wanderly Database",
            defaultextension=".db",
            filetypes=[
                ("SQLite Database", "*.db"),
                ("All files", "*.*")
            ],
            initialfile=(
                "wanderly_backup_"
                + datetime.now().strftime(
                    "%Y%m%d_%H%M"
                )
                + ".db"
            )
        )

        if not filename:
            return

        try:

            shutil.copy2(
                DB_NAME,
                filename
            )

            self.set_status(
                "Database backup created"
            )

            messagebox.showinfo(
                "Backup Complete",
                "Database backup created successfully."
            )

        except Exception as error:

            messagebox.showerror(
                "Backup Error",
                str(error)
            )

    # =========================================================================
    # REFRESH
    # =========================================================================

    def refresh_current_page(self):

        page_map = {
            "dashboard": self.dashboard,
            "packages": self.show_packages,
            "bookings": self.view_bookings,
            "analytics": self.analytics,
            "cancel": self.cancel_booking,
            "data": self.data_center,
            "about": self.about
        }

        command = page_map.get(
            self.current_page,
            self.dashboard
        )

        command()

        self.set_status(
            "Interface refreshed successfully"
        )

    # =========================================================================
    # ABOUT
    # =========================================================================

    def about(self):

        self.clear_content()
        self.set_active_nav("about")
        self.set_status("About Wanderly Elite")

        container, canvas, page = self.create_scrollable(
            self.content
        )

        container.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            page,
            text="About Wanderly Elite ✈",
            font=("Segoe UI", 25, "bold"),
            bg=BG,
            fg=WHITE
        ).pack(
            anchor="w",
            padx=35,
            pady=(30, 5)
        )

        tk.Label(
            page,
            text="A premium Python desktop application for modern travel operations.",
            font=("Segoe UI", 9),
            bg=BG,
            fg=MUTED
        ).pack(
            anchor="w",
            padx=35,
            pady=(0, 20)
        )

        hero = tk.Frame(
            page,
            bg="#0D1A30",
            highlightthickness=1,
            highlightbackground=BORDER_GOLD,
            padx=35,
            pady=30
        )

        hero.pack(
            fill="x",
            padx=35
        )

        tk.Label(
            hero,
            text="WANDERLY ELITE",
            font=("Segoe UI", 24, "bold"),
            bg="#0D1A30",
            fg=GOLD
        ).pack()

        tk.Label(
            hero,
            text="Luxury Travel & Tour Management System",
            font=("Segoe UI", 11),
            bg="#0D1A30",
            fg=WHITE
        ).pack(
            pady=(3, 18)
        )

        tk.Label(
            hero,
            text=(
                "Designed as a complete offline-ready travel management "
                "experience using Python, Tkinter and SQLite."
            ),
            font=("Segoe UI", 10),
            bg="#0D1A30",
            fg=MUTED,
            wraplength=800,
            justify="center"
        ).pack()

        features = [
            (
                "🎨",
                "Premium Interface",
                "Dark luxury visual system with modern cards, navigation and dashboards."
            ),
            (
                "🌍",
                "Destination Explorer",
                "Search, filter and explore curated travel packages."
            ),
            (
                "🎫",
                "Reservation Engine",
                "Create reservations with live traveler-based pricing."
            ),
            (
                "💾",
                "SQLite Database",
                "Store bookings safely using Python's built-in SQLite engine."
            ),
            (
                "📊",
                "Analytics",
                "Review revenue, travelers, package performance and categories."
            ),
            (
                "🛡",
                "Data Management",
                "Export CSV files and create database backups."
            )
        ]

        grid = tk.Frame(
            page,
            bg=BG
        )

        grid.pack(
            fill="x",
            padx=35,
            pady=20
        )

        for index, feature in enumerate(features):

            icon, title, description = feature

            card = tk.Frame(
                grid,
                bg=CARD,
                highlightthickness=1,
                highlightbackground=BORDER,
                padx=18,
                pady=18
            )

            card.grid(
                row=index // 2,
                column=index % 2,
                padx=6,
                pady=6,
                sticky="nsew"
            )

            tk.Label(
                card,
                text=icon,
                font=("Segoe UI Emoji", 24),
                bg=CARD,
                fg=CYAN
            ).pack(
                anchor="w"
            )

            tk.Label(
                card,
                text=title,
                font=("Segoe UI", 11, "bold"),
                bg=CARD,
                fg=WHITE
            ).pack(
                anchor="w",
                pady=(8, 3)
            )

            tk.Label(
                card,
                text=description,
                font=("Segoe UI", 8),
                bg=CARD,
                fg=MUTED,
                wraplength=380,
                justify="left"
            ).pack(
                anchor="w"
            )

        grid.grid_columnconfigure(
            0,
            weight=1
        )

        grid.grid_columnconfigure(
            1,
            weight=1
        )

        technology = tk.Frame(
            page,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=25,
            pady=20
        )

        technology.pack(
            fill="x",
            padx=35,
            pady=(0, 25)
        )

        tk.Label(
            technology,
            text="TECHNOLOGY STACK",
            font=("Segoe UI", 8, "bold"),
            bg=CARD,
            fg=GOLD
        ).pack(
            anchor="w"
        )

        stack = (
            "Python 3.x     •     Tkinter     •     SQLite3     •     CSV     •     "
            "Datetime     •     File Management"
        )

        tk.Label(
            technology,
            text=stack,
            font=("Consolas", 9),
            bg=CARD,
            fg=TEXT
        ).pack(
            anchor="w",
            pady=(8, 0)
        )

        tk.Label(
            technology,
            text=(
                f"Version {APP_VERSION}  •  "
                "Offline Ready  •  Zero External Dependencies"
            ),
            font=("Segoe UI", 8),
            bg=CARD,
            fg=MUTED
        ).pack(
            anchor="w",
            pady=(8, 0)
        )

    # =========================================================================
    # BUTTON FACTORY
    # =========================================================================

    def make_button(
        self,
        parent,
        text,
        command,
        background,
        foreground=WHITE
    ):

        return tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 9, "bold"),
            bg=background,
            fg=foreground,
            activebackground=(
                PRIMARY_HOVER
                if background == PRIMARY
                else "#263A58"
            ),
            activeforeground=WHITE,
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=9
        )

    # =========================================================================
    # KEYBOARD SHORTCUTS
    # =========================================================================

    def bind_shortcuts(self):

        self.root.bind(
            "<Control-b>",
            lambda event: self.open_quick_booking()
        )

        self.root.bind(
            "<Control-d>",
            lambda event: self.dashboard()
        )

        self.root.bind(
            "<Control-p>",
            lambda event: self.show_packages()
        )

        self.root.bind(
            "<Control-r>",
            lambda event: self.refresh_current_page()
        )

        self.root.bind(
            "<Escape>",
            lambda event: self.close_top_window()
        )

    # =========================================================================
    # CLOSE TOP WINDOW
    # =========================================================================

    def close_top_window(self):

        windows = self.root.winfo_children()

        for widget in reversed(windows):

            if isinstance(
                widget,
                tk.Toplevel
            ):

                widget.destroy()
                break

    # =========================================================================
    # EXIT
    # =========================================================================

    def exit_application(self):

        if messagebox.askyesno(
            "Exit Wanderly",
            (
                "Are you sure you want to exit "
                "Wanderly Elite?"
            )
        ):

            self.root.destroy()


# =============================================================================
# APPLICATION STARTUP
# =============================================================================

def main():

    init_database()

    root = tk.Tk()

    app = WanderlyApp(
        root
    )

    root.mainloop()


# =============================================================================
# RUN APPLICATION
# =============================================================================

if __name__ == "__main__":
    main()