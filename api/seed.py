from sqlalchemy.orm import Session

from passlib.hash import bcrypt

from . import models, crud


def seed_initial_data(db: Session):
    statuses_db_check = crud.get_all_statuses(db=db)
    if not statuses_db_check:
        status_new = models.Status(status_name = "New")
        db.add(status_new)
        status_inprogress = models.Status(status_name = "In Progress")
        db.add(status_inprogress)
        status_onhold = models.Status(status_name = "On Hold")
        db.add(status_onhold)
        status_closed = models.Status(status_name = "Closed")
        db.add(status_closed)
        db.commit()
    levels_db_check = crud.get_all_levels(db=db)
    if not levels_db_check:
        level_low = models.Level(level_name = "Low")
        db.add(level_low)
        level_medium = models.Level(level_name = "Medium")
        db.add(level_medium)
        level_high = models.Level(level_name = "High")
        db.add(level_high)
        level_critical = models.Level(level_name = "Critical")
        db.add(level_critical)
        db.commit()
    tickettypes_db_check = crud.get_all_ticket_types(db=db)
    if not tickettypes_db_check:
        ticket_type_incident = models.TicketType(ticket_type_name = "Incident")
        db.add(ticket_type_incident)
        ticket_type_service_request = models.TicketType(ticket_type_name = "Service Request")
        db.add(ticket_type_service_request)
        ticket_type_change_request = models.TicketType(ticket_type_name = "Change Request")
        db.add(ticket_type_change_request)
        db.commit()
    customers_db_check = crud.get_all_customers(db=db)
    if not customers_db_check:
        customer1 = models.Customer(username="Pawel", email="pawel@consulting.eu",
                                    firstname="Pawel", lastname="Kwiatkowski")
        db.add(customer1)
        customer2 = models.Customer(username="Iwona", email="Iwona.Matczewska@gmail.com",
                                    firstname="Iwona", lastname="Matczewska")
        db.add(customer2)
        db.commit()
    agents_db_check = crud.get_all_agents(db=db)
    if not agents_db_check:
        agent1 = models.Agent(username="Admin", email="admin@admin.com",
                                    firstname="Admin", lastname="Admin",
                                    password_hash=bcrypt.hash("zaq1@WSX"))
        agent2 = models.Agent(username="Kacper", email="kacper.dziedzic@wp.pl",
                                    firstname="Kacper", lastname="Dziedzic",
                                    password_hash=bcrypt.hash("zaq1@WSX"))
        db.add(agent1)
        db.add(agent2)
        db.commit()
    tickets_db_check = crud.get_all_tickets(db=db)
    if not tickets_db_check:
        ticket1 = models.Ticket(summary="My Outlook doesn't working", description="Hi, my outlook desktop app is not launching at all, help me pls", customer_id=1, 
                                status_id=1, level_id=1,
                                agent_id=2, ticket_type_id=1)
        db.add(ticket1)
        ticket2 = models.Ticket(summary="Password reset", description="Hi, please reset my password", customer_id=2, 
                                status_id=2, level_id=4,
                                agent_id=2, ticket_type_id=2)
        db.add(ticket2)
        db.commit()