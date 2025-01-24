import pygame

# Pygame initialisieren
pygame.init()

# Fenster erstellen
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Lautstärkeregler")

# Farben
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Musik laden
pygame.mixer.music.load("audio/music.mp3")
pygame.mixer.music.play(-1)  # Endlosschleife
pygame.mixer.music.set_volume(0.5)  # Standardlautstärke

# Schieberegler
slider_x = 150  # Startposition
slider_y = 150
slider_width = 100
slider_height = 5
slider_circle_x = slider_x + 50  # Kreisposition (mittig)
slider_circle_radius = 10

running = True
dragging = False  # Verfolgt, ob der Kreis gezogen wird

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Prüfen, ob der Benutzer auf den Kreis klickt
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (
                slider_circle_x - slider_circle_radius <= mouse_x <= slider_circle_x + slider_circle_radius
                and slider_y - 10 <= mouse_y <= slider_y + 10
            ):
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION and dragging:
            # Slider bewegen
            mouse_x, _ = pygame.mouse.get_pos()
            slider_circle_x = max(slider_x, min(slider_x + slider_width, mouse_x))

            # Lautstärke anpassen
            volume = (slider_circle_x - slider_x) / slider_width
            pygame.mixer.music.set_volume(volume)

    # Bildschirm zeichnen
    screen.fill(WHITE)

    # Slider zeichnen
    pygame.draw.rect(screen, GRAY, (slider_x, slider_y, slider_width, slider_height))
    pygame.draw.circle(screen, RED, (slider_circle_x, slider_y), slider_circle_radius)

    # Lautstärke anzeigen
    font = pygame.font.SysFont(None, 24)
    volume_text = font.render(f"Lautstärke: {pygame.mixer.music.get_volume():.2f}", True, BLACK)
    screen.blit(volume_text, (slider_x, slider_y - 30))

    # Aktualisieren
    pygame.display.flip()

pygame.quit()
