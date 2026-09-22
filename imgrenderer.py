import pygame, os
def loadimgs():
    #load imgs
    chessoldimg = pygame.image.load(os.path.join("Assets/gameboard.png"))
    chessimg = pygame.transform.scale(chessoldimg, (1000, 1000))
    #white pieces
    #King
    wkingoldimg = pygame.image.load(os.path.join("Pieces/white/whiteking.png"))
    wkingimg = pygame.transform.scale(wkingoldimg, (100, 100))
    #Queen
    wqueenoldimg = pygame.image.load(os.path.join("Pieces/white/whitequeen.png"))
    wqueenimg = pygame.transform.scale(wqueenoldimg, (100, 100))
    #Bishop
    wbishopoldimg = pygame.image.load(os.path.join("Pieces/white/whitebishop.png"))
    wbishopimg = pygame.transform.scale(wbishopoldimg, (100, 100))
    #Knight
    wknightoldimg = pygame.image.load(os.path.join("Pieces/white/whiteknight.png"))
    wknightimg = pygame.transform.scale(wknightoldimg, (100, 100))
    #Rook
    wrookoldimg = pygame.image.load(os.path.join("Pieces/white/whiterook.png"))
    wrookimg = pygame.transform.scale(wrookoldimg, (100, 100))
    #Pawn
    wpawnoldimg = pygame.image.load(os.path.join("Pieces/white/whitepawn.png"))
    wpawnimg = pygame.transform.scale(wpawnoldimg, (100, 100))
    #Black Pieces
    #King
    bkingoldimg = pygame.image.load(os.path.join("Pieces/black/blackking.png"))
    bkingimg = pygame.transform.scale(bkingoldimg, (100, 100))
    #Queen
    bqueenoldimg = pygame.image.load(os.path.join("Pieces/black/blackqueen.png"))
    bqueenimg = pygame.transform.scale(bqueenoldimg, (100, 100))
    #Bishop
    bbishopoldimg = pygame.image.load(os.path.join("Pieces/black/blackbishop.png"))
    bbishopimg = pygame.transform.scale(bbishopoldimg, (100, 100))
    #Knight
    bknightoldimg = pygame.image.load(os.path.join("Pieces/black/blackknight.png"))
    bknightimg = pygame.transform.scale(bknightoldimg, (100, 100))
    #Rook
    brookoldimg = pygame.image.load(os.path.join("Pieces/black/blackrook.png"))
    brookimg = pygame.transform.scale(brookoldimg, (100, 100))
    #Pawn
    bpawnoldimg = pygame.image.load(os.path.join("Pieces/black/blackpawn.png"))
    bpawnimg = pygame.transform.scale(bpawnoldimg, (100, 100))