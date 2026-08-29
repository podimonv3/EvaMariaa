import logging
from struct import pack
import re
import base64
from pyrogram.file_id import FileId
from pymongo.errors import DuplicateKeyError
from umongo import Instance, Document, fields
from motor.motor_asyncio import AsyncIOMotorClient
from marshmallow.exceptions import ValidationError
from info import DATABASE_URI, DATABASE_URI2, DATABASE_URI3, DATABASE_NAME, COLLECTION_NAME, USE_CAPTION_FILTER

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]
instance = Instance.from_db(db)

client1 = AsyncIOMotorClient(DATABASE_URI2)
db1 = client1[DATABASE_NAME]
instance1 = Instance.from_db(db1)

client2 = AsyncIOMotorClient(DATABASE_URI3)
db2 = client2[DATABASE_NAME]
instance2 = Instance.from_db(db2)

@instance1.register
class Media(Document):
    file_id = fields.StrField(attribute='_id')
    file_ref = fields.StrField(allow_none=True)
    file_name = fields.StrField(required=True)
    file_size = fields.IntField(required=True)
    file_type = fields.StrField(allow_none=True)
    mime_type = fields.StrField(allow_none=True)
    caption = fields.StrField(allow_none=True)
    
    class Meta:
        indexes = ('$file_name', )
        collection_name = COLLECTION_NAME

@instance2.register
class Mediaa(Document):
    file_id = fields.StrField(attribute='_id')
    file_ref = fields.StrField(allow_none=True)
    file_name = fields.StrField(required=True)
    file_size = fields.IntField(required=True)
    file_type = fields.StrField(allow_none=True)
    mime_type = fields.StrField(allow_none=True)
    caption = fields.StrField(allow_none=True)
    
    class Metaa:
        indexes = ('$file_name', )
        collection_name = COLLECTION_NAME

async def check_file(media):
    """Check if file is present in the database"""

    # TODO: Find better way to get same file_id for same media to avoid duplicates
    file_id, file_ref = unpack_new_file_id(media.file_id)
    
    existing_file = await Media.collection.find_one({"_id": file_id})
    existing_filea = await Mediaa.collection.find_one({"_id": file_id})
    
    if existing_file:
        pass
    elif existing_filea:
        pass
    else:
        okda = "okda"
        return okda
        
async def save_file(media):
    """Save file in database"""

    # TODO: Find better way to get same file_id for same media to avoid duplicates
    file_id, file_ref = unpack_new_file_id(media.file_id)
    file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))
    try:
        file = Media(
            file_id=file_id,
            file_ref=file_ref,
            file_name=file_name,
            file_size=media.file_size,
            file_type=media.file_type,
            mime_type=media.mime_type,
            caption=media.caption.html if media.caption else None,
         )
    except ValidationError:
        logger.exception('Error occurred while saving file in database')
        return False, 2
    else:
        try:
            await file.commit()
        except DuplicateKeyError:      
            logger.warning(
                f'{getattr(media, "file_name", "NO_FILE")} is already saved in database'
            )

            return False, 0
        else:
            logger.info(f'{getattr(media, "file_name", "NO_FILE")} is saved to database')
            return True, 1

async def save_filea(media):
    """Save file in database"""

    # TODO: Find better way to get same file_id for same media to avoid duplicates
    file_id, file_ref = unpack_new_file_id(media.file_id)
    file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))
    try:
        file = Mediaa(
            file_id=file_id,
            file_ref=file_ref,
            file_name=file_name,
            file_size=media.file_size,
            file_type=media.file_type,
            mime_type=media.mime_type,
            caption=media.caption.html if media.caption else None,
       )
    except ValidationError:
        logger.exception('Error occurred while saving file in database')
        return False, 2
    else:
        try:
            await file.commit()
        except DuplicateKeyError:      
            logger.warning(
                f'{getattr(media, "file_name", "NO_FILE")} is already saved in database'
            )

            return False, 0
        else:
            logger.info(f'{getattr(media, "file_name", "NO_FILE")} is saved to database')
            return True, 1
            

async def delete_files_below_threshold(db, threshold_size_mb: int = 50, batch_size: int = 20, chat_id: int = None, message_id: int = None):
    cursor_media = Media.find({"file_size": {"$lt": threshold_size_mb * 1024 * 1024}}).limit(batch_size // 2)
    cursor_mediaa = Mediaa.find({"file_size": {"$lt": threshold_size_mb * 1024 * 1024}}).limit(batch_size // 2)
    deleted_count_media = 0
    deleted_count_mediaa = 0
    
    async for document in cursor_media:
        try:
            await Media.collection.delete_one({"_id": document["file_id"]})
            deleted_count_media += 1
            print(f'Deleted file from Media: {document["file_name"]}')
        except Exception as e:
            print(f'Error deleting file from Media: {document["file_name"]}, {e}')

    async for document in cursor_mediaa:
        try:
            await Mediaa.collection.delete_one({"_id": document["file_id"]})
            deleted_count_mediaa += 1
            print(f'Deleted file from Mediaa: {document["file_name"]}')
        except Exception as e:
            print(f'Error deleting file from Mediaa: {document["file_name"]}, {e}')
            
    deleted_count = deleted_count_media + deleted_count_mediaa
    return deleted_count

async def get_bad_files(query, file_type=None, filter=False):
    """For given query return (results, next_offset)"""
    query = query.strip()

    if not query:
        raw_pattern = '.'
    elif ' ' not in query:
        raw_pattern = r'(\b|[\.\+\-_])' + query + r'(\b|[\.\+\-_])'
    else:
        raw_pattern = query.replace(' ', r'.*[\s\.\+\-_]')

    try:
        regex = re.compile(raw_pattern, flags=re.IGNORECASE)
    except:
        return []

    if USE_CAPTION_FILTER:
        filter = {'file_name': regex}
    else:
        filter = {'file_name': regex}

    if file_type:
        filter['file_type'] = file_type

    total_results_media1 = await Media.count_documents(filter)
    total_results_media2 = await Mediaa.count_documents(filter)
    total_results = total_results_media1 + total_results_media2

    cursor_media1 = Media.find(filter)
    cursor_media1.sort('$natural', -1)
    files_media1 = await cursor_media1.to_list(length=total_results_media1)

    cursor_media2 = Mediaa.find(filter)
    cursor_media2.sort('$natural', -1)
    files_media2 = await cursor_media2.to_list(length=total_results_media2)

    return files_media1, files_media2, total_results



async def get_search_results(query, file_type=None, max_results=10, offset=0, filter=False):
    """For given query return (results, next_offset)"""
    query = query.strip()
    if not query:
        raw_pattern = '.'
    else:
        # ഉപയോക്താവ് തിരയുന്ന വാക്കുകളെ വേർതിരിക്കുന്നു
        keywords = query.split()
        # 1. അക്ഷരത്തെറ്റുകൾ ഉണ്ടെങ്കിലും കണ്ടുപിടിക്കാൻ എല്ലാ വാക്കുകളും '|' (OR) ഇട്ട് തിരയുന്നു
        raw_pattern = "|".join(keywords)

    try:
        regex = re.compile(raw_pattern, flags=re.IGNORECASE)
    except:
        return [], '', 0

    if USE_CAPTION_FILTER:
        filter = {'$or': [{'file_name': regex}, {'caption': regex}]}
    else:
        filter = {'file_name': regex}

    if file_type:
        filter['file_type'] = file_type

    cursor_media = Media.find(filter).sort('$natural', -1)
    cursor_mediaa = Mediaa.find(filter).sort('$natural', -1)

    if offset < 0:
        offset = 0

    # കൂടുതൽ റിസൾട്ടുകൾ എടുത്ത് സോർട്ട് ചെയ്യാൻ വേണ്ടി നീക്കിവെക്കുന്നു
    files_media = await cursor_media.to_list(length=100)
    files_mediaa = await cursor_mediaa.to_list(length=100)

    total_results = len(files_media) + len(files_mediaa)
    interleaved_files = []
    index_media1 = index_media2 = 0
    while index_media1 < len(files_media) or index_media2 < len(files_mediaa):
        if index_media1 < len(files_media):
            interleaved_files.append(files_media[index_media1])
            index_media1 += 1
        if index_media2 < len(files_mediaa):
            interleaved_files.append(files_mediaa[index_media2])
            index_media2 += 1

    # --- മുൻഗണന നിശ്ചയിക്കുന്ന ഭാഗം (Priority Sorting) ---
    def get_priority(file):
        name = file.get('file_name', '').lower()
        caption = file.get('caption', '').lower() if USE_CAPTION_FILTER else ''
        searchable_text = f"{name} {caption}"
        
        keywords_lower = [kw.lower() for kw in keywords]
        
        # എക്സാക്റ്റ് വാക്ക് (ഉദാ: super subbu) അതേപടി ഉണ്ടെങ്കിൽ ഒന്നാം സ്ഥാനം
        if query.lower() in searchable_text:
            return 0
            
        # എല്ലാ വാക്കുകളും ഏതെങ്കിലും ക്രമത്തിൽ ഉണ്ടെങ്കിൽ രണ്ടാം സ്ഥാനം
        if all(kw in searchable_text for kw in keywords_lower):
            return 1
            
        # കൂടുതൽ വാക്കുകൾ മാച്ച് ആകുന്നത് അനുസരിച്ച് മുൻഗണന നൽകുന്നു
        matches = sum(1 for kw in keywords_lower if kw in searchable_text)
        return 2 - (matches / len(keywords_lower))

    # എല്ലാ ഫയലുകളെയും മുൻഗണനാ ക്രമത്തിൽ അടുക്കുന്നു
    interleaved_files.sort(key=get_priority)

    # ഉപയോക്താവ് ആവശ്യപ്പെട്ട ലിമിറ്റ് അനുസരിച്ച് ഫയലുകൾ മുറിച്ചെടുക്കുന്നു
    files = interleaved_files[offset:offset + max_results]
    next_offset = offset + len(files)

    if next_offset < total_results:
        return files, next_offset, total_results
    else:
        return files, '', total_results



async def get_file_details(query):
    filter = {'file_id': query}
    cursor_media = Media.find(filter)
    filedetails_media = await cursor_media.to_list(length=1)
    if filedetails_media:
        return filedetails_media
    # Query details from Mediaa collection
    cursor_mediaa = Mediaa.find(filter)
    filedetails_mediaa = await cursor_mediaa.to_list(length=1)
    if filedetails_mediaa:
        return filedetails_mediaa

def encode_file_id(s: bytes) -> str:
    r = b""
    n = 0

    for i in s + bytes([22]) + bytes([4]):
        if i == 0:
            n += 1
        else:
            if n:
                r += b"\x00" + bytes([n])
                n = 0

            r += bytes([i])

    return base64.urlsafe_b64encode(r).decode().rstrip("=")


def encode_file_ref(file_ref: bytes) -> str:
    return base64.urlsafe_b64encode(file_ref).decode().rstrip("=")


def unpack_new_file_id(new_file_id):
    """Return file_id, file_ref"""
    decoded = FileId.decode(new_file_id)
    file_id = encode_file_id(
        pack(
            "<iiqq",
            int(decoded.file_type),
            decoded.dc_id,
            decoded.media_id,
            decoded.access_hash
        )
    )
    file_ref = encode_file_ref(decoded.file_reference)
    return file_id, file_ref
