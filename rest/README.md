# REST

A REST project that exposes REST end-points that show information about the server's hardware.

# Useful Information
Information that might be useful to an API consumer of this REST service might be RAM, CPU, and storage space.

- RAM would provide useful information that lets the API user know how fast the machine might be able to process information.
- CPU would indicated the age of the technology, how many CPUs and speed of the CPU.  All of these bits of information would also provide insight onto service speed and performance.
- Storge could possibly let the user know how much data the system can store and/or how much data is currently being stored.

# Dynamic Data
Dynamic data could be integrated by establishing a backend database server like MySQL, Mongodb, or PostgreSql.  The application would benefit from leveraging the Model-View-Controller design pattern establishing the Controller and Model layers to handle database transactions.
