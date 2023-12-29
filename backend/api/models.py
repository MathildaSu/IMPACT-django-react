from django.db import models

# Create your models here.


pfeffer_item = [
    ("Normal_0", "0 - Normal"),
    ("Normal_1", "0 - Nunca lo hizo, pero podría hacerlo solo/a"),
    (
        "Con-dificultad_0",
        "1 - Nunca lo hizo y si tuviera que hacerlo ahora tendría dificultad",
    ),
    ("Con-dificultad_1", "1 - Con dificultad, pero se maneja solo"),
    ("Necesita-ayuda", "2 - Necesita ayuda (pero lo hace)"),
    ("Dependiente", "3 - Dependiente (no puede realizarlo)"),
]
screening_items = [
    ("AD8_results", "AD8_results"),
    ("demo_item1", "demo_item1"),
    ("demo_item2", "demo_item2"),
    ("demo_item3", "demo_item3"),
    ("demo_sex", "demo_sex"),
    ("demo_item4", "demo_item4"),
    ("demo_item5", "demo_item5"),
    ("q_item1", "q_item1"),
    ("q_item2", "q_item2"),
    ("q_item3", "q_item3"),
    ("q_item4", "q_item4"),
    ("q_item5", "q_item5"),
    ("q_item6", "q_item6"),
    ("q_item7", "q_item7"),
    ("q_item8", "q_item8"),
    ("rudas_item1", "rudas_item1"),
    ("rudas_item2", "rudas_item2"),
    ("rudas_item3", "rudas_item3"),
    ("rudas_item4", "rudas_item4"),
    ("rudas_item5", "rudas_item5"),
    ("rudas_item6", "rudas_item6"),
    ("rudas_item7", "rudas_item7"),
    ("rudas_item8", "rudas_item8"),
    ("rudas_item9", "rudas_item9"),
    ("rudas_item10", "rudas_item10"),
    ("rudas_item11", "rudas_item11"),
    ("rudas_item12", "rudas_item12"),
    ("rudas_item13", "rudas_item13"),
    ("rudas_item14", "rudas_item14"),
    ("rudas_item15", "rudas_item15"),
    ("rudas_item16", "rudas_item16"),
    ("rudas_item17", "rudas_item17"),
    ("rudas_item18", "rudas_item18"),
    ("pfeffer_item1", "pfeffer_item1"),
    ("pfeffer_item2", "pfeffer_item2"),
    ("pfeffer_item3", "pfeffer_item3"),
    ("pfeffer_item4", "pfeffer_item4"),
    ("pfeffer_item5", "pfeffer_item5"),
    ("pfeffer_item6", "pfeffer_item6"),
    ("pfeffer_item7", "pfeffer_item7"),
    ("pfeffer_item8", "pfeffer_item8"),
    ("pfeffer_item9", "pfeffer_item9"),
    ("pfeffer_item10", "pfeffer_item10"),
    ("pfeffer_item11", "pfeffer_item11"),
]


class Screening(models.Model):
    class Meta:
        ordering = ["-modified_at"]

    id = models.BigAutoField(primary_key=True)
    status = models.CharField(
        max_length=12,
        blank=True,
        choices=[
            ("Completado", "Completado"),
            ("Detenido", "Detenido"),
            ("Pendiente", "Pendiente"),
        ],
    )
    last_filled = models.TextChoices(
        "last_filled",
        screening_items,
    )
    AD8_results = models.BooleanField(blank=True)
    demo_item1 = models.BooleanField(blank=True)
    demo_item2 = models.CharField(
        max_length=8,
        blank=True,
        choices=[
            ("más60", "60 años o más de 60 años"),
            ("menos60", "menos de 60 años"),
        ],
    )
    demo_item3 = models.BooleanField(blank=True)
    demo_sexo = models.CharField(
        max_length=8,
        blank=True,
        choices=[("Mujer", "Mujer"), ("Hombre", "Hombre"), ("Otras", "Otras personas")],
    )
    demo_item4 = models.BooleanField(blank=True)
    demo_item5 = models.BooleanField(blank=True)
    q_item1 = models.CharField(
        max_length=14,
        blank=True,
        choices=[("Si", "Si"), ("No", "No"), ("No-aplicable", "No aplicable")],
    )
    q_item2 = models.CharField(
        max_length=14,
        blank=True,
        choices=[("Si", "Si"), ("No", "No"), ("No-aplicable", "No aplicable")],
    )
    q_item3 = models.CharField(
        max_length=14,
        blank=True,
        choices=[("Si", "Si"), ("No", "No"), ("No-aplicable", "No aplicable")],
    )
    q_item4 = models.CharField(
        max_length=14,
        blank=True,
        choices=[("Si", "Si"), ("No", "No"), ("No-aplicable", "No aplicable")],
    )
    q_item5 = models.CharField(
        max_length=14,
        blank=True,
        choices=[("Si", "Si"), ("No", "No"), ("No-aplicable", "No aplicable")],
    )
    q_item6 = models.CharField(
        max_length=14,
        blank=True,
        choices=[("Si", "Si"), ("No", "No"), ("No-aplicable", "No aplicable")],
    )
    q_item7 = models.CharField(
        max_length=14,
        blank=True,
        choices=[("Si", "Si"), ("No", "No"), ("No-aplicable", "No aplicable")],
    )
    q_item8 = models.CharField(
        max_length=14,
        blank=True,
        choices=[("Si", "Si"), ("No", "No"), ("No-aplicable", "No aplicable")],
    )
    rudas_item1 = models.CharField(
        max_length=10,
        blank=True,
        choices=[("Correcto", "Correcto"), ("Erroneo", "Erroneo")],
    )
    rudas_item2 = models.CharField(
        max_length=10,
        blank=True,
        choices=[("Correcto", "Correcto"), ("Erroneo", "Erroneo")],
    )
    rudas_item3 = models.CharField(
        max_length=10,
        blank=True,
        choices=[("Correcto", "Correcto"), ("Erroneo", "Erroneo")],
    )
    rudas_item4 = models.CharField(
        max_length=10,
        blank=True,
        choices=[("Correcto", "Correcto"), ("Erroneo", "Erroneo")],
    )
    rudas_item5 = models.CharField(
        max_length=10,
        blank=True,
        choices=[("Correcto", "Correcto"), ("Erroneo", "Erroneo")],
    )
    rudas_item6 = models.CharField(
        max_length=10,
        blank=True,
        choices=[("Correcto", "Correcto"), ("Erroneo", "Erroneo")],
    )
    rudas_item7 = models.CharField(
        max_length=10,
        blank=True,
        choices=[("Correcto", "Correcto"), ("Erroneo", "Erroneo")],
    )
    rudas_item8 = models.CharField(
        max_length=10,
        blank=True,
        choices=[("Correcto", "Correcto"), ("Erroneo", "Erroneo")],
    )
    rudas_item9 = models.CharField(
        max_length=14,
        blank=True,
        choices=[
            ("Normal", "Normal"),
            ("Parcialmente", "Parcialmente Adecuado"),
            ("Fallido", "Fallido"),
        ],
    )
    rudas_item10 = models.TextField(blank=True, unique=True)
    rudas_item11 = models.CharField(
        max_length=4, blank=True, choices=[("Si", "Si"), ("No", "No")]
    )
    rudas_item12 = models.CharField(
        max_length=4, blank=True, choices=[("Si", "Si"), ("No", "No")]
    )
    rudas_item13 = models.CharField(
        max_length=4, blank=True, choices=[("Si", "Si"), ("No", "No")]
    )
    """"Q rudas_item 14: What is the difference between a lie and a mistake?" 
    (1) One is intentional, the other is not. 
    (2) One is bad, the other is good (or the older adult just explains one of them). 
    (3) They may answer with anything else or show similarities between them. 
    Abbreviations could be answer 1 = correct, answer 2 = partially correct, and answer 3 = wrong."""
    rudas_item14 = models.CharField(
        max_length=15,
        blank=True,
        choices=[
            ("Correcto", "Cualquier otra cosa, similitudes entre ellas"),
            ("Parcialmente", "Una intencionada, la otra sin intención"),
            (
                "Incorrecto",
                "Una mala, la otra buena o solo explica una de ellas",
            ),
        ],
    )
    rudas_item15 = models.CharField(
        max_length=15,
        blank=True,
        choices=[
            (
                "Correcto",
                "Buscarlo en la agenda de teléfonos, en la guía de teléfonos de la ciudad, ir a alguna municipalidad o dependencia a pedir información, llamar a un amigo en común)",
            ),
            (
                "Parcialmente",
                "Llamar a la policía, llamar a telefónica (normalmente no dan la dirección)",
            ),
            ("Incorrecto", "Sin respuesta clara"),
        ],
    )
    rudas_item16 = models.JSONField(blank=True, null=True)
    rudas_item17 = models.IntegerField(default=0, blank=True)
    rudas_item18 = models.TextField(blank=True, unique=True)
    pfeffer_item1 = models.CharField(max_length=16, blank=True, choices=pfeffer_item)
    pfeffer_item2 = models.CharField(max_length=16, blank=True, choices=pfeffer_item)
    pfeffer_item3 = models.CharField(max_length=16, blank=True, choices=pfeffer_item)
    pfeffer_item4 = models.CharField(max_length=16, blank=True, choices=pfeffer_item)
    pfeffer_item5 = models.CharField(max_length=16, blank=True, choices=pfeffer_item)
    pfeffer_item6 = models.CharField(max_length=16, blank=True, choices=pfeffer_item)
    pfeffer_item7 = models.CharField(max_length=16, blank=True, choices=pfeffer_item)
    pfeffer_item8 = models.CharField(max_length=16, blank=True, choices=pfeffer_item)
    pfeffer_item9 = models.CharField(max_length=16, blank=True, choices=pfeffer_item)
    pfeffer_item10 = models.CharField(max_length=16, blank=True, choices=pfeffer_item)
    pfeffer_item11 = models.CharField(max_length=16, blank=True, choices=pfeffer_item)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class StudyPartner(models.Model):
    id = models.UUIDField(primary_key=True)
    # older_adult_associated = models.ForeignKey(OlderAdult)
    nombre = models.TextField(blank=False)
    appelido = models.TextField(blank=False)
    consent = models.BooleanField(default=False)
    telephone = models.TextField(blank=True)
    email = models.TextField(blank=True)
    address = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class OlderAdult(models.Model):
    id = models.UUIDField(primary_key=True)
    nombre = models.TextField(blank=False)
    appelido = models.TextField(blank=False)
    status = models.CharField(
        max_length=12,
        blank=True,
        choices=[
            ("Completado", "Completado"),
            ("Detenido", "Detenido"),
            ("Pendiente", "Pendiente"),
        ],
    )
    AD8 = models.CharField(
        max_length=12,
        blank=True,
        choices=[
            ("Positive", "Positive"),
            ("Negative", "Negative"),
        ],
    )
    idioma = models.TextField(
        blank=True,
        null=True,
    )
    consent = models.BooleanField(default=False)
    study_partner = models.ForeignKey(
        StudyPartner,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    # community_worker = models.ManyToManyField(
    #     CommunityWorker,
    #     blank=True,
    #     null=True,
    # )
    region = models.TextField(blank=False)
    telephone = models.TextField(blank=True)
    email = models.TextField(blank=True)
    image = models.TextField(blank=True)
    address = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Visit(models.Model):
    class Meta:
        ordering = ["-created_at"]

    id = models.BigAutoField(primary_key=True)
    screen_id = models.ForeignKey(
        Screening,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    older_adults = models.ForeignKey(
        OlderAdult,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    # community_worker = models.ManyToManyField(CommunityWorker)
    status = models.CharField(
        max_length=12,
        blank=True,
        choices=[
            ("Completado", "Completado"),
            ("Detenido", "Detenido"),
            ("Pendiente", "Pendiente"),
            ("Planeada", "Planeada"),
        ],
    )
    duratioin = models.IntegerField(default=0)
    safety_rating = models.IntegerField(default=0, blank=False)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CommunityWorker(models.Model):
    id = models.UUIDField(primary_key=True)
    nombre = models.TextField(blank=False)
    appelido = models.TextField(blank=False)
    visit_id = models.ManyToManyField(
        Visit,
        blank=True,
        related_name="visit_id",
    )
    older_adults: models.ManyToManyField(
        OlderAdult,
        blank=True,
        related_name="older_adults",
    )
    region = models.TextField(blank=False)
    n_attempt_visit = models.IntegerField(default=0)
    n_completed_visit = models.IntegerField(default=0)
    certificate_status = models.CharField(
        max_length=6,
        blank=True,
        choices=[
            ("Base", "Base"),
            ("Adv", "Advanced"),
            ("Pro", "Professional"),
        ],
    )
    telephone = models.TextField(blank=False, unique=True)
    email = models.TextField(blank=False, unique=True)
    image = models.TextField(blank=True)
    address = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
