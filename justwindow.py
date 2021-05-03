""" justwindow.py """

import sys
import pygame
from pygame.locals import QUIT


def list_sns(region, creds, sns_topics=[]):
    sns = boto_session('sns', creds, region)
    response = sns.list_topics()
    for topic_arn in response["Topics"]:
        sns_topics.append(topic_arn["TopicArn"])
    return sns_topics
  
def process():
    for region, creds in jobs["auth_config"]:
        arns = list_sns(region, creds)
    return

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
pygame.display.set_caption("Just Window")

def main():
    """ main routine """
    while True:
        SURFACE.fill((255, 255, 255))

        for event at pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main()

