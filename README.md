# 🚨 Resq Now — Smart Emergency & Accident Reporting System

**Report road accidents. Share location. Help emergency responders act faster.**

Resq Now is a web-based emergency reporting platform designed to improve coordination during road accidents. It allows witnesses or bystanders to report accidents by uploading photographic evidence, sharing their current location and providing an optional description.

The submitted information is stored in a centralized database, helping emergency response teams access accident reports and coordinate their response.

## 🌐 Live Demo

**Application:** https://resq-now-573d.vercel.app/

## ✨ Features

### 🚑 Public Accident Reporting
- Report road accidents without requiring an account.
- Capture accident photographs using a device camera.
- Upload existing images as evidence.
- Automatically capture the current geographical location using browser geolocation.
- Add an optional accident description.
- Submit accident reports to the backend.

### 🔐 Official Authentication
- Dedicated login interface for emergency personnel.
- Supabase Authentication integration.
- Existing official accounts for ambulance and police personnel.
- Role-based access control (under development).

### 📊 Emergency Management
- Centralized storage of accident reports.
- Official dashboard interface.
- Accident status management.
- Ambulance and police response coordination (under development).

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| React 19 | Frontend library |
| TypeScript | Type safety |
| Vite | Development server and build tool |
| Tailwind CSS | Styling |
| Supabase | Backend and database |
| Supabase Auth | Official authentication |
| Supabase Storage | Accident image storage |
| Vercel | Deployment |

## 🏗️ System Overview

```text
          Witness / Bystander
                  |
                  v
          Resq Now Web App
                  |
          +-------+-------+
          |       |       |
          v       v       v
        Photo   Location Description
          |       |       |
          +-------+-------+
                  |
                  v
             Supabase
          +-------+-------+
          |       |       |
          v       v       v
        Storage Database Auth
          |       |       |
          +-------+-------+
                  |
                  v
          Emergency Officials
          (Ambulance / Police)
```

## ⚙️ Getting Started

Follow these instructions to run the project locally.

### Prerequisites

- Node.js (LTS version recommended)
- npm
- Git
- A Supabase project

### 1. Clone the Repository

```bash
git clone https://github.com/nabeelbs098/Resq_Now.git
```

### 2. Navigate to the Project

```bash
cd Resq_Now
```

### 3. Install Dependencies

```bash
npm install
```

If npm reports a peer dependency conflict with React Day Picker, use:

```bash
npm install --legacy-peer-deps
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
VITE_SUPABASE_URL=your_supabase_project_url
VITE_SUPABASE_PUBLISHABLE_KEY=your_supabase_publishable_key
```

Replace the placeholder values with your Supabase project credentials.

**Security:** Never expose your Supabase service-role key in frontend code or commit private credentials to GitHub.

### 5. Start the Development Server

```bash
npm run dev
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:5173
```

### 6. Build for Production

```bash
npm run build
```

## 🗄️ Database

Resq Now uses Supabase as its backend.

The current database includes:

### Officials Table

Stores emergency personnel information.

| Column | Description |
|---|---|
| `id` | Official UUID |
| `name` | Official name |
| `role` | Official role, such as ambulance or police |
| `email` | Official email address |

### Reports Table

Stores submitted accident reports.

The application uses Supabase to persist accident information and associated evidence.

## 📁 Project Structure

```text
Resq_Now/
│
├── public/
├── src/
│   ├── components/
│   │   └── ui/
│   ├── hooks/
│   ├── integrations/
│   │   └── supabase/
│   ├── lib/
│   ├── pages/
│   │   ├── Dashboard.tsx
│   │   ├── Index.tsx
│   │   ├── Login.tsx
│   │   └── NotFound.tsx
│   ├── App.tsx
│   └── main.tsx
│
├── .env
├── package.json
├── tsconfig.json
└── vite.config.ts
```

## 🚀 Future Improvements

- Complete role-based dashboards for emergency personnel.
- Real-time ambulance location tracking.
- Automatic assignment of nearby emergency responders.
- Live emergency notifications.
- Hospital coordination and response management.
- Improved emergency analytics and reporting.

## 🎯 Project Objective

The main objective of Resq Now is to reduce delays in accident reporting and improve communication between witnesses and emergency response teams.

By combining location services, image uploads and centralized data management, the platform aims to make emergency coordination faster and more accessible.

## 👨‍💻 Developer

**Nabeel B S**

B.Tech Computer Science and Engineering Student

- GitHub: https://github.com/nabeelbs098

---

**Resq Now — Every Second Matters.** 🚨
