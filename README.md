# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram


### Flowchart of the main workflow

```mermaid
flowchart TD
    A[Start App] --> B{Login as Student or Admin}
    B -->|Student| C[Enter Student ID or 'new']
    C --> D{Existing ID?}
    D -->|Yes| E[Student Menu]
    D -->|No| F[Create Profile] --> E

    E --> E1[View Course Catalog]
    E --> E2[Register for Course]
    E --> E3[Drop Course]
    E --> E4[View Schedule]
    E --> E5[Billing Summary]
    E --> E6[Edit Profile]
    E --> E7[Logout and Save]
    E7 --> G[Back to Login]

    B -->|Admin| H[Enter Admin Password]
    H --> I{Password correct?}
    I -->|Yes| J[Admin Menu]
    I -->|No| G

    J --> J1[View Course Catalog]
    J --> J2[View Class Roster]
    J --> J3[View All Students]
    J --> J4[Add New Student]
    J --> J5[Edit Student Profile]
    J --> J6[Add New Course]
    J --> J7[Edit Course]
    J --> J8[View Student Schedule]
    J --> J9[Billing Summary for Student]
    J --> J10[Logout and Save]
    J10 --> G

    G -->|Continue| B
    G -->|Exit| K[Exit App]
```

### Prompts
"I select the use case "Create New student Profile", so your task is to create an equivalent Python version of the program. Put the Python program in a new folder called “python.”, Note that I want only "create new student profile" function. Do not include other funtionalities"