from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre', models.CharField(db_index=True, max_length=60)),
                ('sede_principal', models.CharField(max_length=45)),
                ('descripcion', models.TextField()),
                ('sitio_web', models.URLField(blank=True, null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_usuario', models.ImageField(blank=True, null=True, upload_to='usuarios/')),
                ('nombre', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45, unique=True)),
                ('contrasenia', models.CharField(max_length=100)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Valoraciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntualidad', models.IntegerField(default=0)),
                ('seguridad', models.IntegerField(default=0)),
                ('economica', models.IntegerField(default=0)),
                ('amabilidad', models.IntegerField(default=0)),
                ('caro', models.IntegerField(default=0)),
                ('inseguro', models.IntegerField(default=0)),
                ('impuntual', models.IntegerField(default=0)),
                ('poco_amables', models.IntegerField(default=0)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_ENVIA_YA.empresas')),
            ],
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_ENVIA_YA.departamentos')),
            ],
        ),
        migrations.CreateModel(
            name='Estrellas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estrella_1', models.IntegerField(default=0)),
                ('estrella_2', models.IntegerField(default=0)),
                ('estrella_3', models.IntegerField(default=0)),
                ('estrella_4', models.IntegerField(default=0)),
                ('estrella_5', models.IntegerField(default=0)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_ENVIA_YA.empresas')),
            ],
        ),
        migrations.CreateModel(
            name='Distritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_ENVIA_YA.provincias')),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.TextField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_ENVIA_YA.empresas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_ENVIA_YA.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='AgenciasLima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_referencial', models.CharField(max_length=100)),
                ('foto', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(max_length=100)),
                ('link_mapa', models.CharField(max_length=200)),
                ('horario_de_atencion', models.CharField(max_length=45)),
                ('telefono', models.CharField(max_length=20)),
                ('cochera', models.BooleanField(blank=True, null=True)),
                ('distritos', models.ManyToManyField(related_name='agencias', to='API_ENVIA_YA.distritos')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_ENVIA_YA.empresas')),
            ],
        ),
    ]
